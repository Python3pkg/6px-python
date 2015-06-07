import httplib, json, base64, mimetypes, socket, os, thread, string

import websocket

from .output import Output
from .result import Result, ResultInfo

from urlparse import urlparse

class cloud6:

	@staticmethod
	def init(user_id = None, api_key = None, api_secret = None):
		"""
		Factory method to create a new cloud6 request
		"""

		return cloud6(
			os.getenv('CLOUD6_USER_ID', user_id),
			os.getenv('CLOUD6_API_KEY', api_key),
			os.getenv('CLOUD6_API_SECRET', api_secret)
		)

	"""
	Represents a single cloud6 request
	"""
	def __init__(self, user_id, api_key, api_secret):
		self.user_id = user_id
		self.api_key = api_key
		self.api_secret = api_secret
		self.images = {}
		self.outputs = []
		self.callback = None
		self.url = None

		self.job_finished = None

		self.version = '0.0.1'

		def handleIncoming(ws, message):
			res = json.loads(message)

			if "status" in res and res['status'] == 'complete':
				self.job_finished = res['job_id']
				ws.close()

		def handleSocketOpen(ws):
			ws.send(json.dumps({ 'auth': { 'user_id': self.user_id } }))

		def handleSocketError(ws, error):
			pass
			# print "Socket Error:", error

		def handleSocketClose(ws):
			pass
			# print "Socket connection closed"

		self.ws = websocket.WebSocketApp("ws://socks.cloud6.io/",
			on_message = handleIncoming,
			on_error = handleSocketError,
			on_close = handleSocketClose
		)

		self.ws.on_open = handleSocketOpen

		thread.start_new_thread(self.ws.run_forever, ())

	def output(self, refs):
		out = Output(refs)
		self.outputs.append(out)

		return out

	def load(self, name, image):
		"""
		Sets our input image
		"""

		self.images[name] = image

		return self

	def callback(self, url):
		"""
		Set a callback URL for whenever the job is done
		"""

		self.callback = url

		return self


	def type(self, mime):
		"""
		Set the destination mimetype of our image
		"""

		self.type = mime

		return self

	def get_info(self):

		refs = {}
		for key, value in self.images.iteritems():
			refs[key] = False

		self.output(refs).tag('info')

		res = self.save()

		return ResultInfo(res)

	def get_output_by_tag_name(self, tag):
		for output in self.outputs:
			if output.tagName == tag:
				return output

		return None

	def save(self):
		"""
		Make our call to cloud6 to process your job
		"""

		inputs = {}
		for key, value in self.images.iteritems():
			inputs[key] = self.parse_input(value)

		outputs = []
		for output in self.outputs:
			outputs.append(output.export())

		data = {
			'input': inputs,
			'output': outputs
		}

		if self.callback is not None:
			data['callback'] = {
				'url': 'http://cloud6.io'
			}

		response = json.loads(self.request("post", "/users/:userId/jobs", json.dumps(data)))

		waiting = True

		# want to wait until the job is actually finished
		while waiting:
			if self.job_finished == response['id']:
				waiting = False

		return Result(json.loads(self.request("get", "/users/:userId/jobs/" + response["id"])))

	def parse_input(self, input):
		"""
		Converts our input to a base64 encoded string
		"""

		o = urlparse(input)

		# its a URL and not a file
		if o.scheme:
			return input

		with open(input, "rb") as image:
		    encoded = base64.b64encode(image.read())
		    return 'data:'+ mimetypes.guess_type(input)[0] + ';base64,' + encoded

	def request(self, method, path, data = None):
		"""
		Makes our HTTP request to cloud6
		"""

		conn = httplib.HTTPSConnection('api.cloud6.io')

		path = path.replace(':userId', self.user_id)

		conn.request(method.upper(), '/v1/'+ path + '?key='+ self.api_key + '&secret='+ self.api_secret, data, {
			'Content-Type': 'application/json',
			'User-Agent': 'cloud6 Python SDK '+ self.version
		})

		res = conn.getresponse()

		status = res.status
		reason = res.reason

		r = res.read()

		conn.close()

		return r

import httplib, json, base64, mimetypes

class PX:
	@staticmethod
	def init(user_id, api_key, api_secret):
		"""
		Factory method to create a new 6px request
		"""

		return PX(user_id, api_key, api_secret)

	"""
	Represents a single 6px request
	"""
	def __init__(self, user_id, api_key, api_secret):
		self.user_id = user_id
		self.api_key = api_key
		self.api_secret = api_secret
		self.image = None
		self.callback = None
		self.tag = None
		self.type = 'image/png'
		self.version = '0.0.4'
		self.hasFilters = False
		self.actions = []
		self.filters = {}

	def load(self, image):
		"""
		Sets our input image
		"""

		self.image = image

		return self

	def resize(self, size):
		"""
		Sets an action to our image to resize given the width and height given
		"""

		self.actions.append({ 'method': 'resize', 'options': size })

		return self

	def filter(self, type, value):
		"""
		Sets image filters to our image
		"""

		self.hasFilters = True

		self.actions['filter'][type] = value

		return self

	def rotate(self, options):
		"""
		Rotates our input image
		"""

		self.actions.append({ 'method': 'rotate', 'options': options })

		return self

	def crop(self, position):
		"""
		Crops our image to given coordinates or to the dominate face
		"""

		self.actions.append({ 'method': 'crop', 'options': position })

		return self

	def callback(self, url):
		"""
		Set a callback URL for whenever the job is done
		"""

		self.callback = url

		return self

	def tag(self, tag):
		"""
		Sets the tag for our input image
		"""

		self.tag = tag

		return self

	def type(self, mime):
		"""
		Set the destination mimetype of our image
		"""

		self.type = mime

		return self

	def save(self):
		"""
		Make our call to 6px to proess our job
		"""

		uri = self.parse_input(self.image)

		if self.hasFilters:
			self.actions.append({ 'method': 'filter', 'options': self.filters })


		data = {
			'input': { 'main': uri },
			'priority': 0,
			'user_id': self.user_id,
			'output': [{
				'ref': [ 'main' ],
				'type': self.tag,
				'methods': self.actions
			}]
		}

		if self.tag is not None:
			data['output']['tag'] = self.tag

		if self.callback is not None:
			data['output']['callback'] = {
				'url': 'http://6px.io'
			}

		response = self.send(json.dumps(data))

		print response

	def parse_input(self, input):
		"""
		Converts our input to a base64 encoded string
		"""

		with open(input, "rb") as image:
		    encoded = base64.b64encode(image.read())
		    return 'data:'+ mimetypes.guess_type(input)[0] + ';base64,' + encoded

	def send(self, data):
		"""
		Makes our HTTP request to 6px
		"""

		conn = httplib.HTTPConnection('https://api.6px.io/v1', 443)
		
		conn.request('POST', '/users/'+ self.user_id + '/jobs?key='+ self.api_key + '&secret='+ self.api_secret, data, {
			'Content-Type': 'application/json',
			'User-Agent': '6px Python SDK '+ self.version
		})

		res = conn.getresponse()

		status = res.status
		reason = res.reason

		data = res.read()

		conn.close()

		return data


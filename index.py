import httplib, json, base64, mimetypes

class PX:
	@staticmethod
	def init(user_id, api_key, api_secret):
		return PX(user_id, api_key, api_secret)

	def __init__(self, user_id, api_key, api_secret):
		self.user_id = user_id
		self.api_key = api_key
		self.api_secret = api_secret
		self.image = None
		self.callback = None
		self.actions = {}

	def load(self, image):
		self.image = image

		return self

	def resize(self, size):
		self.actions['resize'] = size

		return self

	def filter(self, type, value):
		if 'filter' not in self.actions:
			self.actions['filter'] = {}

		self.actions['filter'][type] = value

		return self

	def priority(self, number):
		self.priority = number

		return self

	def rotate(self, options):
		self.actions['rotate'] = options

		return self

	def crop(self, position):
		self.actions['crop'] = position

		return self

	def callback(self, url):
		self.callback = url

		return self

	def save(self):

		uri = self.parse_input(self.image)

		data = {
			'input': [uri],
			'priority': 0,
			'user_id': self.user_id,
			'output': [{
				'ref': [0],
				'tag': 'heyo',
				'type': 'image/png',
				'methods': [self.actions]
			}]
		}

		if self.callback is not None:
			data['callback'] = {
				'url': 'http://6px.io'
			}

		response = self.send(json.dumps(data))

		print response

	def parse_input(self, input):
		with open(input, "rb") as image:
		    encoded = base64.b64encode(image.read())
		    return 'data:'+ mimetypes.guess_type(input)[0] + ';base64,' + encoded

	def send(self, data):

		conn = httplib.HTTPConnection('http://api.6px.io', 80)
		
		conn.request('POST', '/users/'+ self.user_id + '/jobs?key='+ self.api_key + '&secret='+ self.api_secret, data, {
			'Content-Type': 'application/json'
		})

		res = conn.getresponse()

		status = res.status
		reason = res.reason

		data = res.read()

		conn.close()

		return data


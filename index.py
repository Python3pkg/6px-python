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

		return

	def save(self):

		uri = self.parse_input(self.image)

		output = json.dumps({
			'input': [uri],
			'callback': {
				'url': 'http://6px.io'
			},
			'priority': 0,
			'user_id': self.user_id,
			'output': [{
				'ref': [0],
				'tag': 'heyo',
				'type': 'image/png',
				'methods': [self.actions]
			}]
		})

		response = self.send(output)

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



if __name__ == '__main__':

	px = PX.init(
		user_id='51df7563ece2e10000000002', 
		api_key='152463ce1bdb025128205d0a0bdb1ab5', 
		api_secret='5a617c03b76e49f60d3a685132f5b4b5'
	)
	px.load('/Users/dustin/Pictures/astronaut.jpg')
	px.resize({ 'width': 200, 'height': 400 })
	px.save()

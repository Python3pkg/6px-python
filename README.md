6px-python-sdk
==============

Simple usage:

	import px
	
	px = PX.init(
		user_id='YOUR USER ID', 
		api_key='YOUR API KEY', 
		api_secret='YOUR API SECRET'
	)
	px.load('/path/to/picture.jpg')
	px.resize({ 'width': 200, 'height': 400 })
	px.save()
Python library for 6px
======================

Python library for interacting with the 6px API. This module includes methods to make the process of sending images to 6px for processing easier.

## Getting Started

```bash
$ sudo pip install px
```

## Simple Usage

	from _6px import PX

	px = PX.init(
		user_id='YOUR USER ID',
		api_key='YOUR API KEY',
		api_secret='YOUR API SECRET'
	)

	px.load('img', '/path/to/picture.jpg')

	out = px.output({ 'img': False })
	out.resize({ 'width': 200, 'height': 400 })

	px.save()

More examples of what is possible can be found by visiting the [6px API documentation](https://github.com/6px-io/6px-api-docs)

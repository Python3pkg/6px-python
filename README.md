Python library for 6px
======================

Python library for interacting with the [6px API](http://6px.io). This library includes methods that makes sending image processing jobs to 6px easier.

## Getting Started

Install Pip:
```bash
$ pip install px
```
Sudo-chop if necessary...
##Examples
If you want to simply upload an image to the 6px CDN:
```python
from _6px import PX

px = PX.init(
    user_id='YOUR USER ID',
    api_key='YOUR API KEY',
    api_secret='YOUR API SECRET'
)

px.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = px.output({ 'taxi': 'unsplashed_taxi' })
out.tag('raw').url('6px');

px.save()
```

Given that vintage photos are kind of kind of popular right now, let's take this up a notch:
```python
from _6px import PX

px = PX.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

px.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = px.output({ 'taxi': 'unsplashed_taxi' })
out.tag('vintage')
	.url('6px')
	.filter({ sepia: 70 });

px.save()
```
So, we have a bit of an extreme sepia effect going on here, but that's fine.  I think this deserves to be more of a thumbnail.  We are going to resize it now:
```python
from _6px import PX

px = PX.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

px.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = px.output({ 'taxi': 'unsplashed_taxi' })
out.tag('vintage_thumb')
	.url('6px')
	.filter({ sepia: 70 })
	.resize({ width: 75 });

px.save()
```
Another thing we can do is change the dominate color of an image:
```python
from _6px import PX

px = PX.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

px.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = px.output({ 'taxi': 'unsplashed_taxi' })
out.tag('green')
	.url('6px')
	.filter({colorize: { hex: '#00FF00', strength: 80 }});

px.save()
```
Let's blur the image at the same time.
```python
from _6px import PX

px = PX.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

px.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = px.output({ 'taxi': 'unsplashed_taxi' })
out.tag('green_blur')
	.url('6px')
	.filter({
		colorize: { hex: '#00FF00', strength: 80 },
		stackBlur: 20
	});

px.save()
```
Now that we have covered some of the simple use cases, feel free to refer to our documentation!

##[API Documentation](https://github.com/6px-io/6px-api-docs)

Keep us posted on the cool stuff you are doing by sending us an email at <ops@6px.io>. We are constantly trying to improve the user experience. If you come across any issues or have suggestions please create an [issue ticket.](https://github.com/6px-io/6px-python/issues)

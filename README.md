Python library for cloud6
======================

Python library for interacting with the [cloud6 API](http://cloud6.io). This library includes methods that makes sending image processing jobs to cloud6 easier.

## Getting Started

Install Pip:
```bash
$ pip install cloud6
```
Sudo-chop if necessary...
##Examples
If you want to simply upload an image to the cloud6 CDN:
```python
from _cloud6 import cloud6

cloud6 = cloud6.init(
    user_id='YOUR USER ID',
    api_key='YOUR API KEY',
    api_secret='YOUR API SECRET'
)

cloud6.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = cloud6.output({ 'taxi': 'unsplashed_taxi' })
out.tag('raw').url('cloud6');

cloud6.save()
```

Given that vintage photos are kind of kind of popular right now, let's take this up a notch:
```python
from _cloud6 import cloud6

cloud6 = cloud6.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

cloud6.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = cloud6.output({ 'taxi': 'unsplashed_taxi' })
out.tag('vintage')
	.url('cloud6')
	.filter({ sepia: 70 });

cloud6.save()
```
So, we have a bit of an extreme sepia effect going on here, but that's fine.  I think this deserves to be more of a thumbnail.  We are going to resize it now:
```python
from _cloud6 import cloud6

cloud6 = cloud6.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

cloud6.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = cloud6.output({ 'taxi': 'unsplashed_taxi' })
out.tag('vintage_thumb')
	.url('cloud6')
	.filter({ sepia: 70 })
	.resize({ width: 75 });

cloud6.save()
```
Another thing we can do is change the dominate color of an image:
```python
from _cloud6 import cloud6

cloud6 = cloud6.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

cloud6.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = cloud6.output({ 'taxi': 'unsplashed_taxi' })
out.tag('green')
	.url('cloud6')
	.filter({colorize: { hex: '#00FF00', strength: 80 }});

cloud6.save()
```
Let's blur the image at the same time.
```python
from _cloud6 import cloud6

cloud6 = cloud6.init(
	user_id='YOUR USER ID',
	api_key='YOUR API KEY',
	api_secret='YOUR API SECRET'
)

cloud6.load('taxi', 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg')

out = cloud6.output({ 'taxi': 'unsplashed_taxi' })
out.tag('green_blur')
	.url('cloud6')
	.filter({
		colorize: { hex: '#00FF00', strength: 80 },
		stackBlur: 20
	});

cloud6.save()
```
Now that we have covered some of the simple use cases, feel free to refer to our documentation!

##[API Documentation](https://github.com/cloud6/cloud6-api-docs)

Keep us posted on the cool stuff you are doing by sending an email to <support@cloud6.io>. If you come across any issues or have suggestions please [open an issue on GitHub](https://github.com/cloud6/cloud6-node/issues).

[![Analytics](https://ga-beacon.appspot.com/UA-44211810-2/cloud6-python)](https://github.com/igrigorik/ga-beacon)

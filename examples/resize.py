from _cloud6 import cloud6

cloud6 = cloud6.init()

cloud6.load('taxi', './images/unsplash_city_taxi.jpg')
cloud6.load('logo', 'http://cloud6.io/img/px-logo-md@2x.png')

out = cloud6.output({ 'taxi': False })

out.resize({ 'width': 250 })
out.tag('taxi')
out.url('cloud6')

res = cloud6.save()
print res.get_output('taxi').get_location('taxi')

# get the width using the get_info convenience call
cloud6 = cloud6.init()
print cloud6.load('taxi', './images/unsplash_city_taxi.jpg').get_info().get_width('taxi')

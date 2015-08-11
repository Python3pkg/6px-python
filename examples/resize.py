from _6px import 6px

6px = 6px.init()

6px.load('taxi', './images/unsplash_city_taxi.jpg')
6px.load('logo', 'http://6px.io/img/px-logo-md@2x.png')

out = 6px.output({ 'taxi': False })

out.resize({ 'width': 250 })
out.tag('taxi')
out.url('6px')

res = 6px.save()
print res.get_output('taxi').get_location('taxi')

# get the width using the get_info convenience call
6px = 6px.init()
print 6px.load('taxi', './images/unsplash_city_taxi.jpg').get_info().get_width('taxi')

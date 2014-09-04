from _6px import PX

px = PX.init()

px.load('taxi', './images/unsplash_city_taxi.jpg')
px.load('logo', 'http://6px.io/img/px-logo-md@2x.png')

out = px.output({ 'taxi': False })

out.resize({ 'width': 250 })
out.tag('taxi')
out.url('6px')

res = px.save()
print res.get_output('taxi').get_location('taxi')

# get the width using the get_info convenience call
px = PX.init()
print px.load('taxi', './images/unsplash_city_taxi.jpg').get_info().get_width('taxi')

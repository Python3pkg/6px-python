from _6px import PX

px = PX.init(
    api_key="***API_KEY***",
    api_secret="***API_SECRET***",
    user_id="***USER_ID***"
)

px.load('taxi', './images/unsplash_city_taxi.jpg')
px.load('logo', 'http://6px.io/img/px-logo-md@2x.png')

out = px.output({ 'taxi': False })

out.resize({ 'width': 250 })
out.tag('taxi')
out.url('6px')

px.save()

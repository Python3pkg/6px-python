import imp

px = imp.load_source('PX', '../px/__init__.py')

PX = px.PX.init(
    api_key="***API_KEY***",
    api_secret="***API_SECRET***",
    user_id="***USER_ID***"
)

PX.load('taxi', './images/unsplash_city_taxi.jpg')
PX.load('logo', 'http://6px.io/img/px-logo-md@2x.png')

out = PX.output({ 'taxi': False })

out.resize({ 'width': 250 })
out.tag('taxi')
out.url('6px')

PX.save()

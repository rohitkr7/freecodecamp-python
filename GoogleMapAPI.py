import urllib.request
import urllib.parse
import urllib.error
import json


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location:')
    if(len(address)) < 1:
        break

    # Note this program will need an API key to be attached in the url to work
    '''
    https: // maps.googleapis.com / maps / api / geocode / json?address = 1600 + Amphitheatre + Parkway,
    +Mountain + View, +CA & key = YOUR_API_KEY
    '''
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    finally:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retireve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)

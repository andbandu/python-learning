import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'


address = input('Enter location: ')
if len(address) < 1:
    address = 'University of Helsinki'


url = serviceurl + urllib.parse.urlencode({'q': address})
print('Retrieving', url)


uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')


try:
    js = json.loads(data)
except:
    js = None

if not js or 'features' not in js or len(js['features']) == 0:
    print('==== Failure To Retrieve ====')
else:
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)
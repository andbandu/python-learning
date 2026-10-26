import urllib.request, urllib.parse, urllib.error
import json

# Base URL for the py4e API endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Prompt for the location
address = input('Enter location: ')
if len(address) < 1:
    address = 'University of Helsinki'

# Construct the full URL with urlencoded parameters
url = serviceurl + urllib.parse.urlencode({'q': address})
print('Retrieving', url)

# Open the URL and read the response
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

# Extract the plus_code from the JSON structure
if not js or 'features' not in js or len(js['features']) == 0:
    print('==== Failure To Retrieve ====')
else:
    # Navigate the GeoJSON structure to find the plus_code
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)
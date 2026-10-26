import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors (useful for https URLs)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_2479180.json '

print('Retrieving', url)


uh = urllib.request.urlopen(url, context=ctx)
data = json.loads(uh.read())
print('User count:', len(data['comments']))

total_sum = 0

for item in data['comments']:
    total_sum += int(item['count'])

print('Sum:', total_sum)


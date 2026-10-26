import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors (useful for https URLs)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_2479179.xml'

print('Retrieving', url)


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')


tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))


total_sum = 0
for count in counts:
    total_sum += int(count.text)

print('Sum:', total_sum)
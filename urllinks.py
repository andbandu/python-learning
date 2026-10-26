import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p) != script_dir]

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/known_by_Minah.html"
count = 7
position = 18




for i in range(count):
    print("Retrieving:", url)
    

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    
    target_tag = tags[position - 1]
    
    url = target_tag.get('href', None)
    
print("Retrieving:", url)
print("Last name retrieved:", target_tag.contents[0])
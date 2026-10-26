import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir in sys.path:
    sys.path.remove(script_dir)

import urllib.request
from bs4 import BeautifulSoup



url = "http://py4e-data.dr-chuck.net/comments_2479177.html"
html = urllib.request.urlopen(url, timeout=10).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0

for tag in tags:
    count += int(tag.text)

print("Total:", count)

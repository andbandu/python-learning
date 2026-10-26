import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for line in fhand:
    print(line.decode().strip())

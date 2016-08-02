import json
from urllib.request import urlopen

url = 'http://www.json.org/example.html'
response = urlopen(url)
contents = response.read()
print(contents)
# text = contents.decode('utf8')
# data = json.load(text)
# for video in data['feed']['entry'][0:6]:
#     print (video['title']['$t'])
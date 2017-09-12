import requests
import json

r=requests.get('https://api.github.com/events')
#print r.json()

#J.son Data Parsing
#print r.json()

print r.json()["payload"]


#print r.json()[0]['payload']

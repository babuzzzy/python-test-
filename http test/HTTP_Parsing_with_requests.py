# coding=utf_8
import requests

#r = requests.get('http://httpbin.org/ip')

#print(r.text)
#print(r.status_code)

payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=payload)

print(r.url)
print(r.text)
print(r.status_code)

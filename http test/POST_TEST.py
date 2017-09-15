import httplib, urllib

conn = httplib.HTTPConnection("httpbin.org") # Do not use "http://"

params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn.request("POST", "/post", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data

params = "test string"
headers = {"Content-type": "text/html"}
conn.request("POST", "/post", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data

conn.close()

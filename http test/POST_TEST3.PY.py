import httplib, urllib
params = urllib.urlencode({'spam':1, 'eggs':  2, 'bacon':0})
headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
conn=httplib.HTTPConnection("httpbin.org")
conn.request("POST","/post", params, headers)
response = conn.getresponse()
print response.status
print response.read()

import httplib

conn = httplib.HTTPConnection("httpbin.org")

conn.request("GET", "/xml")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1

conn.request("GET", "/get")
r2 = conn.getresponse()
print r2.status, r2.reason
data2 = r2.read()
print data2

conn.close()

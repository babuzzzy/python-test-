import httplib

conn = httplib.HTTPConnection("httpbin.org")

conn.request("GET", "ip")
r1 = conn.getresponse()
print r1.status, r1.reason

conn.request("GET","/get")
r2 = conn.getresponse()
print r2.status, r2.reason

data2 = r2.read()
print data2

conn.close()


import httplib

conn = httplib.HTTPConnection('httpbin.org')
conn.putrequest("GET","/get")
conn.putheader('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
#conn.putheader('User-Agent','Mozilla/5.0(Windows; u; windows NT 6.1;en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome//5.0.375.126 Safari//5.33.4')
#conn.putheader('Accept-Encoding','gzip,deflate,sdch')
#conn.putheader('Accept-Language','en-US,en;q=0.8')
#conn.putheader('Accept-Charset','ISO-8859-1,utf-8;1=0.7,*;q=0.3')
conn.endheaders()
r1= conn.getresponse()
print r1.read()

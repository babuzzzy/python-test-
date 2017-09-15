import httplib

conn=httplib.HTTPConnection("m.spam.kt.com")

headers={
    "Upgrade-Insecure-Requests: 1",
    "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"
}
conn.putrequest("GET","mSpam_04_01.asp?SelSearchType=&SearchWord=&qStartDate=&qEndDate=&TabIDX=3&pageno=1&Key2=20170812251250&Key1=2")
conn.putheader("Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
conn.putheader("Accept-Encoding:gzip, deflate")
conn.putheader("Accept-Language:ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4")
conn.putheader("Cache-Control:max-age=0")
conn.endheaders()
r1=conn.getresponse()

print r1.read()


# coding=utf_8
#한글주석

import httplib

conn = httplib.HTTPConnection("devnauts.tistory.com")

f= open('result12.txt','w')
conn.request("GET", "/112")
r1 = conn.getresponse()
print r1.status
print r1.reason

data1 = r1.read()

f.write(data1)

# 미션 1. 출력결과를 메모장에 저장하기
# 미션 2. 출력괄과 중 특정 부분만 파싱해서 저장하기
# 미션 2. 출력결과 중 한글만 추려서 메모장에 저장하기
print data1

conn.close()
f.closed()

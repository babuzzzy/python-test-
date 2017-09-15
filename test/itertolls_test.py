# -*-coding:utf_8-*-
import itertools
import random
import httplib
import re, string


letters =['a','b','c','d','e','f']
booleans = [1,0,1,0,0,1]
decimals = [0.1,0.7,0.4,0.5]

#print list(itertools.chain(letters, booleans, decimals))
characters='7012835964'

print list(itertools.product(characters,repeat = 2))

#random.sample()

num=open('test.txt','w')
#num.write(test)
num.close()
#print list(itertools.product([1,2,3],[3,4]))


#print list(itertools.product([7012835964],repeat=8))


def getString(length=8, characters='7012835964'): ## 123456789 를 넣는 것보다 이게 효율적인가
    for hp in itertools.product(characters, repeat=length):
        yield ' '.join(random.sample(hp,8))

for hp in getString():
    conn = httplib.HTTPConnection("www.naver.com")
    conn.putrequest("GET","/kun/index.aspx?TAB=2")
    conn.putheader("HTTP_PHONE_NUMEBER",'82010'+hp) #82010 은 고정된 값이고 나머지를 변경
    conn.putheader("HTTP_DEVICE_INFO","LX:240,LY:320,CL:8,SX:98,SY:88,SC:8")
    conn.endheaders()





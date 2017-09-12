# coding=utf-8
# 문자열에 공백이나 문장부호가 있어도, 오직 문자열 만 가지고 palindrome 을 판별해 나가기

## 만약 문자열에 공백이 있으면 없는 걸로 치환
def remove1(text):
    if ' ' in text:
        print 'text'

#def remove2(text)

text=raw_input('input text : ')
remove1(text)

print text

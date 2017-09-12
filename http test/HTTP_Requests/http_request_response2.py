# coding=utf_8
import string, random
#i=0

max = 10
alphabet = string.letters[0:26] + string.digits

print string.letters #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print string.digits #0123456789
print string.letters[0:26] #abcdefghijklmnopqrstuvwxyz
print alphabet #abcdefghijklmnopqrstuvwxyz0123456789

for count in xrange (0,max):
    string = ''
    for x in random.sample(alphabet,random.randint(8,8)): # randint는 지정한 범위에서의 난수를 생성 1:7 은 1부터 7까지 난수를 생선함
        string += x
    print string
    #i+=1
    #if i == 10:
    #    break




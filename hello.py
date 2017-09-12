#coding=cp949
#coding=utf-8

age = 20
name = 'Swaroop'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'why is {0} playing with that python'.format(name)


print '{} was {} years old when he wrote this book'.format(name, age)
print 'why is {} playing with that python'.format(name)

print name + 'is ' + str(age) +' years old'

# 소수점 이하 넷째 자리까지 부동 소숫점 숫자 표기 (0.3333)
print '{0:.4f}'.format(1.0/3)
# 밑줄(_)로 17 칸을 채우고 가운데 정렬(^)하기
print '{0:_^17}'.format('hello')
print '{name} worte {book}'.format(name='Swaroop',
                                       book='A byte of python')

print 'this is the first linet굈this'

print 'this is the test line 굈 test line ddddd'


print "What's your name"

print 'whats굚 your name_2'

print r"newlines are indicated by 굈"

print 'this is the first line굈 this is the second line'


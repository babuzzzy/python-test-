#coding=cp949
#coding=utf-8

age = 20
name = 'Swaroop'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'why is {0} playing with that python'.format(name)


print '{} was {} years old when he wrote this book'.format(name, age)
print 'why is {} playing with that python'.format(name)

print name + 'is ' + str(age) +' years old'

# �Ҽ��� ���� ��° �ڸ����� �ε� �Ҽ��� ���� ǥ�� (0.3333)
print '{0:.4f}'.format(1.0/3)
# ����(_)�� 17 ĭ�� ä��� ��� ����(^)�ϱ�
print '{0:_^17}'.format('hello')
print '{name} worte {book}'.format(name='Swaroop',
                                       book='A byte of python')

print 'this is the first linet�nthis'

print 'this is the test line �n test line ddddd'


print "What's your name"

print 'whats�� your name_2'

print r"newlines are indicated by �n"

print 'this is the first line�n this is the second line'


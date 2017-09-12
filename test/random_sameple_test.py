# coding:utf_8
import random
import itertools

numlist = [1,2,3,4,5,6,7,8,9,10]
s = random.sample(numlist,8)
print s


def getString(length=8, characters='7012835964'): ## 123456789 를 넣는 것보다 이게 효율적인가
    for hp in itertools.product(characters, repeat=length):
        yield ' '.join(random.sample(hp,8))





# -*- coding: utf-8 -*-
# 모든 파이썬 모듈은 name 속성을 가지고 있다.
# 만약 __name__  속성이 __main__ 일 경우, 이것은 모듈이 사용자로부터 직접 실행된 것을 의미한다.

if __name__ =='__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

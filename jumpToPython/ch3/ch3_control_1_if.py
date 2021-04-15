# -*- encoding: utf-8

money = True
if money:
    print "Texi"
else:
    print "Walk"
print ""

"""
비교연산자	    설명
x < y	    x가 y보다 작다
x > y	    x가 y보다 크다
x == y	    x와 y가 같다
x != y	    x와 y가 같지 않다
x >= y	    x가 y보다 크거나 같다
x <= y	    x가 y보다 작거나 같다


연산자	    설명
x or y	    x와 y 둘중에 하나만 참이면 참이다
x and y	    x와 y 모두 참이어야 참이다
not x	    x가 거짓이면 참이다


in	        not in
x in 리스트	x not in 리스트
x in 튜플	x not in 튜플
x in 문자열	x not in 문자열
"""

# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')

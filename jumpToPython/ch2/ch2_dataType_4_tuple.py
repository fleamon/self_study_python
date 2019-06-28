#!/usr/bin/env python
# -*- encoding: utf-8

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print "t1 : " + str(t1)
print "t2 : " + str(t2)
print "t3 : " + str(t3)
print "t4 : " + str(t4)
print "t5 : " + str(t5)
print t1
print t2
print t3
print t4
print t5

print t3[2]
print t4[1]
print t5[2]
print t5[2][1]
# del t5[2][1] -- ERROR : Tuple can not delete parameter.
# t3[1] = 4 -- ERROR : Tuple can not modify parameter.

print t3 + t4
print t3 * 2
print len(t3)

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 튜플 추가"
t = (1, 2, 3)
print t
print t + (4,)

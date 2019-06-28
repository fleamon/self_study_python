#!/usr/bin/env python
# -*- encoding: utf-8

s1 = set([1,2,3])
print s1
# print s1[0]
# TypeError: 'set' object does not support indexing
s2 = set("Hello")
print s2
# print s2[1]
# TypeError: 'set' object does not support indexing
print ""
print list(s1)
print list(s1)[1]
print list(s2)
print list(s2)[1]
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print s1 & s2
print s1.intersection(s2)
print s1 | s2
print s1.union(s2)
print s1 - s2
print s2 - s1
print s1.difference(s2)
print s2.difference(s1)
print ""
s1 = set([1, 2, 3])
print s1
s1.add(4)
print s1
s1.update([5, 6, 7])
print s1
s1.remove(6)
print s1
s1.remove(7)
print s1

print ""
print ""
print ""

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 집합의 중복"
a = set([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5])
print a
print "2. 집합 만들기"
a = {}
print type(a)
a = set()
print type(a)

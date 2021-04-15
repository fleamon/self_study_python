# -*- encoding: utf-8

from copy import copy

# 변수명 = 변수에 저장할 값

print "A = B <-- In this case, A is just refference for B at list"
a = [1, 2, 3]
b = a
print id(a)
print id(b)
print id(a) == id(b)
print a
print b
a[1] = 10
print a
print b
print ""

print id(a)
a = 1
print id(a)
a = 'a'
print id(a)
print ""

print "A = B[:] <-- In this case, REAL COPY at list"
a = []
b = []
a = [1, 2, 3]
print a
b = a[:]
print b
a[1] = 10
print a
print b
print ""

a = []
b = []
print a
print b
a = [1, 2, 3]
b = copy(a)
print a
print b
print ""

a, b = ('python', 'life')
print a
print type(a)
print b
print type(b)
(a, b) = ('python', 'life')
print a
print type(a)
print b
print type(b)
[a, b] = ['python', 'life']
print a
print type(a)
print b
print type(b)
a = b = 'python'
print a
print type(a)
print b
print type(b)
a = 3
b = 5
print a
print b
a, b = b, a
print a
print b

print ""
print ""
print ""

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 변수와 객체"
a = [1, 2, 3]
b = [1, 2, 3]
print a is b
print a == b
b = a
print a is b
print a == b
print "is --> for same refference"
print "== --> for same value"
print ""
print "2. 리스트의 더하기와 extend"
a = [1, 2, 3]
a = a + [4, 5]
print a
b = [1, 2, 3]
b.extend([4, 5])
print b
print a is b
print a == b

# -*- encoding: utf-8

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print "a : " + str(a)
print "b : " + str(b)
print "c : " + str(c)
print "d : " + str(d)
print "e : " + str(e)
print ""
print b[0]
print b[1] + b[2]
print e[-1]
print e[-1][0]
print e[-1][1]
print b[0:2]
print c[:2]
print c[2:]
print c + e
print b * 3
print len(b)
print len(b) + len(d)
print b
b[1] = 10
print b
del b[1]
print b
b.append(2)
print b
del b[1:]
print b
b.append(2)
print b
b.append(3)
print b
a = [2, 6, 5, 4, 9, 8]
a.sort()
print a
a.reverse()
print a
a.remove(5)
print a
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print b.index(2)
# print b.index(5) -- ERROR
print b
b.insert(0, 100)
print b
b.remove(100)
print b
b.insert(1, 100)
print b
b.pop(1)
print b
print b.count(1)
b.append(1)
b.append(1)
print b
print b.count(1)
b.pop(3)
print b
b.pop(3)
print b
b.extend([4, 5])
print b
b.extend(d)
print b

print ""
print ""
print ""

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 리스트 조인"
a = ['Life', 'is', 'too', 'short']
print a
print " ".join(a)
print "2. 리스트 정렬"
a = [1, 3, 5, 4, 2]
print a
a.sort()
print a
a.reverse()
print a

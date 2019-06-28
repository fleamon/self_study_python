#!/usr/bin/env python
# -*- encoding: utf-8

a = "python"
for i in a:
    print i
print ""

a = ['one', 'two', 'three']
for i in a:
    print i
print ""

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print first + last
print ""

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print "%d번 학생은 %d점으로 합격입니다" % (number, mark)
    else:
        print "%d번 학생은 %d점으로 불합격입니다" % (number, mark)
print ""

a = range(10)
print a
a = range(5, 10)
print a
print ""
sum = 0
for i in range(1, 11):
    sum = sum + i
print sum
print ""

marks = [90, 25, 67, 45, 80]
number = 0
for mark in range(len(marks)):
    number = number + 1
    if marks[mark] >= 60:
        print "%d번 학생은 %d점으로 합격입니다" % (number, marks[mark])
    else:
        print "%d번 학생은 %d점으로 불합격입니다" % (number, marks[mark])
print ""

for i in range(2, 10):
    for j in range(1, 10):
        print str(i) + " * " + str(j) + " = " + str(i * j)
    print ""
print ""

a = [1, 2, 3, 4]
res = []
print a
for i in a:
    res.append(i*5)
print res
print ""

a = [1, 2, 3, 4]
res = []
print a
res = [i * 3 for i in a]
print res
print ""

a = [1, 2, 3, 4]
res = []
print a
res = [i * 10 for i in a if i % 2 == 0]
print res

print ""
print ""
print ""

# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 1부터 100까지 출력"
for i in range(1, 101):
    print i
print ""
print "2. 학급의 평균점수"
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
s = 0
avg = 0.0
for i in A:
    s = s + i
avg = s / len(A)
print "A학급의 총점은 %d, 평균은 %d 입니다." % (s, avg)
print ""
print "3. 리스트 내포"
number = [1, 2, 3, 4, 5]
result = [i * 2 for i in number if i % 2 == 1]
print result

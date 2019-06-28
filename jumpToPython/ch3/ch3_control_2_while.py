#!/usr/bin/env python
# -*- encoding: utf-8

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print "나무를 %d 번 찍었습니다." % treeHit
    if treeHit == 10:
        print "나무 넘어갑니다."
print ""

prompt = """
1. Add
2. Del
3. List
4. Quit
"""
number = 0
while number != 4:
    print "prompt1"
    print prompt
    #number = raw_input()
    #number = input()
    #number = int(raw_input())
    number = int(input())

number = 0
while 1:
    print "prompt2"
    print prompt
    number = int(input())
    if number == 4:
        break


# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 3의 배수의 합"
res = 0
number = 0
while number < 1000:
    number = number + 1
    if number % 3 == 0:
        res = res + number
print res
print ""
print "2. 50점 이상의 총합"
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
res = 0
while A:
    tmp = A.pop()
    if tmp >= 50:
        res = res + tmp
print res
print ""
print "3. 별표시하기"
cnt = 0
while cnt < 4:
    cnt = cnt + 1
    print "*" * cnt

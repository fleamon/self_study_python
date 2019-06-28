#!/usr/bin/env python
#-*- encoding: utf-8

import os.path

f = open("new_file.txt", 'w')
# 상대경로가능
# f = open("./../new_file.txt", 'w')
# 절대경로가능
# f = open("/Users/kakao/Applications/python-workspace/wooneo_MW/jumpToPython/new_file.txt", 'w')
for i in range(1, 11):
    # data = "%d번째 줄입니다.\n" % i
    # f.write(data)
    f.write("%d번째 줄입니다.\n" % i)
f.close()

f = open("new_file.txt", 'r')
line = f.readline()
print line
f.close()
print ""

f = open("new_file.txt", 'r')
while 1:
    line = f.readline()
    if not line:
        break
    print line
f.close()
print ""

f = open("new_file.txt", 'r')
lines = f.readlines()
print lines
f.close()
print ""

f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
    print line
f.close()
print ""

f = open("new_file.txt", 'r')
data = f.read()
print data
f.close()
print ""

f = open("new_file.txt", 'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("new_file.txt", 'r')
data = f.read()
print data
f.close()
print ""

with open("new_file.txt", 'w') as f:
    f.write("Jenna, I'm wooneo. Will you marry me?\n")
with open("new_file.txt", 'r') as f:
    f.readline()
    print f
    # <open file 'new_file.txt', mode 'r' at 0x10e55a4b0>
print ""
print ""
print ""

# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 파일 읽고 출력하기"
f1 = open("num1.txt", 'w')
f1.write("Life is too short")
f1.close() # answer : need to close for saving
f2 = open("num1.txt", 'r')
print(f2.read())
print ""
print "2. 파일저장"
if not os.path.isfile("num2.txt"):
    f = open("num2.txt", 'w')
    data = raw_input("입력값 : ")
    f.write(data + "\n")
else:
    f = open("num2.txt", 'a')
    data = raw_input("입력값 : ")
    f.write(data + "\n")
f.close()
print ""
print "3. 역순저장"
f = open("num3.txt", 'r')
lines = f.readlines()
f.close()
lines.reverse()
f = open("num3.txt", 'w')
for line in lines:
    line.strip()
    f.write(line)
f.close()
print ""
print "4. 파일 수정"
f = open("num4.txt", 'r')
data = f.read()
f.close()
# print data
if 'java' in data:
    data = data.replace('java', 'python')
elif 'python' in data:
    data = data.replace('python', 'java')
# print data
f = open("num4.txt", 'w')
f.write(data)
f.close()
print ""
print "5. 평균값 구하기"
f = open("num5.txt", 'r')
lines = f.readlines()
f.close()
s = 0
cnt = 0
for line in lines:
    cnt = cnt + 1
    s = s + int(line)
f = open("num5.txt", 'a')
f.write("총합 : " + str(s) + "\n")
f.write("평균 : " + str(s / cnt) + "\n")
f.close()
print ""

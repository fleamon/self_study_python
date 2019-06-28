#!/usr/bin/env python
# -*- encoding: utf-8

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print dic
a = {1: 'hi'}
print a
a = {'a': [1,2,3]}
print a

a = {1: 'a'}
print a
# print a[0] -- ERROR
print a[1]
a[2] = 'b'
print a
a['name'] = 'wooneo'
print a
del a[1]
print a
job = {"김연아":"피겨스케이팅", "박찬호":"야구", "박지성":"축구", "귀도":"파이썬"}
print job['김연아']
print job['박찬호']
print ""
print dic
print dic['name']
print dic['phone']
print dic['birth']
a = {1:'a', 1:'b'}
print a
print ""
print ""
print dic
print dic.keys()
print dic.values()
for idx in dic.keys():
    print idx
print list(dic.keys())
print list(dic.values())
print dic.items()
print dic.items()[0]
print dic.items()[1]
print dic.items()[2]
# print dic.items()[3] -- ERROR
print dic
dic.clear()
print dic
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print "woodfkjalsdfjalksdfalskfklsadjfasdf"
print dic['name']
print dic.get('name')
print "woodfkjalsdfjalksdfalskfklsadjfasdf"

# print dic['aaa'] -- ERROR
print dic.get('aaa')
print dic.get('aaa', '없음')
print 'name' in dic
print 'aaa' in dic
print 'phone' in dic
print 'phone ' in dic

print ""
print ""
print ""

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 딕셔녀리 만들기"
dic = {'name':'홍길동','birth':'1128','age':30}
print dic
print "2. 딕셔너리 오류"
a = dict();
print a
a['name'] = 'python'
print a
a[('a',)] = 'python'
print a
# a[[1]] = 'python'
# print a
a[250] = 'python'
print a
print "3. 딕셔너리 값 추출"
a = {'A':90, 'B':80}
print a.get('C', 70)

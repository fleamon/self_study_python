#-*- encoding: utf-8

print abs(2)
print abs(-2)
print abs(02)
print abs(-1.2)
print abs(0)
print ""
print all([1, 2, 3])
print all([1, 2, 0])
print ""
print any([1, 2, 3])
print any([1, 2, 0])
print any(["", 1, 2])
print any(["", 0, 1])
print any(["", 0])
print ""
print chr(45)
print chr(65)
print ""
print dir([1, 2, 3])
print ""
print divmod(1, 2)
print divmod(7, 3)
print ""
for i, name in enumerate(['body', 'foo', 'bar']):
    print i, name
print eval("1+2")
print type(eval("1+2"))
print eval("'hi, ' + 'wooneo'")
print type(eval("'hi, ' + 'wooneo'"))
print ""
def positive(x):
    return x > 0
print filter(positive, [0, 1, 5, -1, -8, 7])
print ""
print hex(1)
print hex(10)
print hex(15)
print hex(16)
print ""
print id(1)
print ""
"""
a = input("입력 : ")
print type(a)
a = raw_input("입력 : ")
print type(a)
"""
print ""
print int("3")
print int(3)
print int(3.1)
print int('10', 2)
print int('1B', 16)
print int('43', 5)
print ""
class Person: pass
a = Person()
b = 1
print isinstance(a, Person)
print isinstance(b, Person)
print ""
print len("12345")
print len([1, 2, 3])
print len((1, 2))
print ""
print list("Python")
print type(list("Python"))
print list([1, 2, 3])
print type(list([1, 2, 3]))
print list((1, 2))
print type(list((1, 2)))
print ""
def two_times(x):
    return x * 2
print list(map(two_times, [1, 2, 3, 4, 5]))
print ""
print max([1, 2, 3, 4, 5])
print max("python")
print min([1, 2, 3, 4, 5])
print min("python")
print ""
print oct(10)
print oct(8)
print oct(16)
print oct(38840)
print ""
"""
mode	설명
w	    쓰기 모드로 파일 열기
r	    읽기 모드로 파일 열기
a	    추가 모드로 파일 열기
b	    바이너리 모드로 파일 열기
"""
print ord("A")
print ord("a")
print ord("\n")
print ord(" ")
print ord("\t")
print ""
print pow(2, 4)
print pow(3, 3)
print ""
print range(5)
print range(2, 7)
print range(0, 10, 3)
print ""
print round(1.2)
print round(-1.2)
print round(1.12345, 2)
print round(-1.12345, 3)
print ""
print sorted([3, 1, 2])
print sorted(["a", "c", "b"])
print sorted("wooneo")
print ""
a = "123"
print type(a)
a = 123
print type(a)
print str(a)
print type(str(a))
print ""
print sum([1, 2, 3])
print sum((1, 2))
print ""
print tuple("abc")
print type(tuple("abc"))
print tuple((1, 2, 3))
print type(tuple((1, 2, 3)))
print ""
print list(zip([1, 2, 3], [4, 5, 6]))
print list(zip([1, 2, 3], [4, 5, 6]))
print list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print list(zip(['a', 'b', 'c'], ['d', 'e', 'f']))
print list(zip("wooneo", "jenna"))
print ""

print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1-1. 결과예측1"
print all([1, 2, abs(-3)-3])
print "1-2. 결과예측2"
print chr(ord('a')) == 'a'
print ""
print "2. filter 와 index"
lambda1 = lambda x: x > 0
print list(filter(lambda1, [1, -2, 3, -5, 8, -3]))
print list(filter(lambda x: x < 0, [1, -2, 3, -5, 8, -3]))
print ""
print "3. 16진수를 10진수로 변환"
print int("0xea", 16)
print ""
print "4. map과 lambda"
lambda1 = lambda x: x * 3
print list(map(lambda1, [1, 2, 3, 4]))
print list(map(lambda x: x * 3, [1, 2, 3, 4, 5]))
print ""
print "5. 최대값과 최소값"
print max([-8, 2, 7, 5, -3, 5, 0, 1])
print min([-8, 2, 7, 5, -3, 5, 0, 1])
print max([-8, 2, 7, 5, -3, 5, 0, 1]) + min([-8, 2, 7, 5, -3, 5, 0, 1])
print ""
print "6. 소수점 반올림"
print 17/3.0
print round(float(17/3.0), 4)

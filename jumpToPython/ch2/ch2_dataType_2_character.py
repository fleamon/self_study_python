# -*- coding:utf-8 -*-
a = 'Life is too short, You need Python'
print(a)
print(a[0])
print(a[0:4])
print(a[5:])
print(a[:11] + ' fun.')
print(a[0:-6] + 'love.')
print(a[-6:])
print(a[-6:-4])
print''
print(a[0:11] + '%s' + a[-15:-6] + '%s') % (' short', 'python.')
"""
코드	설명
%s	문자열 (String)
%c	문자 1개(character)
%d	정수 (Integer)
%f	부동소수 (floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
"""
print "Jenna %10s" % "hi"
print "%-10s Jenna" % "hi"

print "%0.4f" % 3.42132111
print "%10.4f" % 1.229958
print "%-10.4f" % -11.138384 + "end"

print "I eat {0} apples".format(3)
print "I eat {0} apples".format("three")
print ""

number = 3
print "I eat {0} apples".format(number)
numberStr = "Three"
print "I eat {0} apples".format(numberStr)
print "I eat {0} apples, You will eat {1} grapes".format(number, numberStr)
print "I eat {number} apples, You will eat {numberStr} grapes".format(number=5, numberStr="Seven")
print ""
print "{0:<20}".format("HI")
print "{0:>20}".format("Jenna")
print "{0:^50}".format("Will you marry me?")
print ""
print ""
print ""
print "Function For Literal"
sentence = "Wooneo said, Will you marry me? Jenna."
print sentence.count("a")
print sentence.find("W")
print sentence.find("w")
print sentence.__len__()
print len(sentence)
print sentence.index("W")
# print sentence.index("w") # -- ERROR
print ""
print ""
print ""
print ",".join("abcd")
print ", ".join("abcd")
print ",".join(['a', 'b', 'c', 'd'])
print ", ".join(['a', 'b', 'c', 'd'])
print "I love you, Jenna.".upper()
print "I love you, Jenna.".lower()
print "   I love you, Jenna.   ".lstrip()
print "   I love you, Jenna.   ".rstrip()
print "   I love you, Jenna.   ".strip()
a = "Life is too short"
print a.replace("Life", "인생")
print a
print a.split()
print a.split(" ")

print ""
print ""
print ""
# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print "1. 문자열나누기"
pin = "881120-1068234"
print pin.split("-")[0]
print pin.split("-")[1]
print "2. 문자열 인덱싱"
print pin.split("-")[1][0]
print "3. 문자열 바꾸기"
a = "a:b:c:d"
print a.replace(":", "#")
print "4. 문자열 바꾸기2"
a = "a:b:c:d"
print "#".join(a.split(":"))

#-*- encoding: utf-8

"""
No such file or directory
division by zero
index out of range
"""

# f = open("test.txt", "r")
# Error : No such file or directory

try:
    f = open("test.txt", "r")
except:
    print "파일없음"

# print 4 / 0
# Error : division by zero
try:
    print 4 / 0
except:
    print "0으로 나눌 수 없음"

a = [1, 2]
# print a[2]
# Error : list index out of range
try:
    print a[2]
except:
    print "리스트 범위 벗어남"

print ""

try:
    print a[2]
    print 4/0
except ZeroDivisionError:
    print "0으로 나눌 수 없음"
except IndexError:
    print "리스트 범위 벗어남"
finally:
    print "끝!"

print ""

try:
    print a[1]
    print 4/0
except ZeroDivisionError as e:
    print e
except IndexError as e:
    print e
finally:
    print "끝!"

print ""

try:
    print a[2]
    print 4/0
except (ZeroDivisionError, IndexError) as e:
    print e
finally:
    print "끝!"

print ""

try:
    f = open("test.txt", "r")
except IOError:
    print "pass"
    pass

print ""

# raise NotImplemented
# raise Error

class MyError(Exception):
    print "MyError"

def include_str(str):
    if 'error' in str:
        raise MyError()
    else:
        return str

print include_str("good job")
# print include_str("good error") -- MyError

print ""

try:
    include_str("good job")
    include_str("good error")
except MyError:
    print "MyError"

print ""

print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 예외처리"

# print [1, 2, 3][3]
# print "a"+1
# print 4 / 0

result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print result


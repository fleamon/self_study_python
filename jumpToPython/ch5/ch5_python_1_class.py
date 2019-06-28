#!/usr/bin/env python
#-*- encoding: utf-8

res1 = 0
def add(num):
    global res1
    res1 = res1 + num
    return res1
print add(3)
print add(4)

res2 = 0
def add2(num):
    global res2
    res2 = res2 + num
    return res2
print add2(2)
print add2(3)

print """
If you need some calculator in one block?
If you can make it once and reuse it?
"""

class Cal:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num
        return self.result

    def sub(self, num):
        self.result = self.result - num
        return self.result

cal1 = Cal()
cal2 = Cal()
cal3 = Cal()

print cal1.add(3)
print cal1.add(4)
print cal2.add(2)
print cal2.add(3)
print cal3.sub(10)
print cal3.sub(5)
print ""

class FourCalc:
    def __init__(self):
        self.result = 0.0
    def add(self, num):
        self.result = self.result + num
        return self.result
    def sub(self, num):
        self.result = self.result - num
        return self.result
    def mul(self, num):
        self.result = self.result * num
        return self.result
    def div(self, num):
        self.result = self.result / num
        return self.result

a = FourCalc()
print a.add(10)
print a.sub(5)
print a.sub(2)
print a.mul(2)
print a.div(5)
print a.div(2)
print ""

class MoreFourCalc(FourCalc):
    def pow(self, num):
        self.result = self.result ** num
        return self.result

b = MoreFourCalc()
print b.add(10)
print b.sub(5)
print b.sub(2)
print b.mul(2)
print b.div(5)
print b.div(2)
print b.pow(2)
print ""

class CalClass:
    def setData(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        res = self.num1 + self.num2
        return res
    def sub(self):
        res = self.num1 - self.num2
        return res
    def mul(self):
        res = self.num1 * self.num2
        return res
    def div(self):
        res = float(self.num1) / float(self.num2)
        return res

a = CalClass()
a.setData(3.1, 2)
print a.add()
print a.sub()
print a.mul()
print a.div()
print ""

class CalClass2(CalClass):
    def pow(self):
        res = self.num1 ** self.num2
        return res

b = CalClass2()
b.setData(5, 2)
print b.add()
print b.sub()
print b.mul()
print b.div()
print b.pow()
print ""

class CalClass3(CalClass2):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            res = self.num1 / self.num2
            return res

c = CalClass3()
c.setData(5, 0)
print c.add()
print c.sub()
print c.mul()
print c.div()
print c.pow()
print ""

class Family:
    lastname = "백"

print Family.lastname
f = Family()
f2 = Family()
print f.lastname
print f2.lastname
print id(Family.lastname)
print id(f.lastname)
print id(f2.lastname)
print ""

class LookPart:
    def __init__(self, data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.score = tmp[2]
    def print_age(self):
        print "%s의 나이는 %s살 입니다." % (self.name, self.age)
    def print_grade(self):
        if int(self.score) >= 90:
            grade = 'A'
        elif int(self.score) >= 80 and int(self.score) < 90:
            grade = 'B'
        elif int(self.score) >= 70 and int(self.score) < 90:
            grade = 'C'
        elif int(self.score) >= 60 and int(self.score) < 90:
            grade = 'D'
        else:
            grade = 'E'
        print "%s의 나이는 %s이고, 점수는 %s로 등급은 %s입니다." % (self.name, self.age, self.score, grade)

d1 = LookPart("wooneo|33|95")
d2 = LookPart("luke|41|89")
d3 = LookPart("archer|33|72")
d4 = LookPart("james|30|67")
d5 = LookPart("who|26|55")

d1.print_age()
d2.print_age()
d3.print_age()
d4.print_age()
d5.print_age()
print ""
d1.print_grade()
d2.print_grade()
d3.print_grade()
d4.print_grade()
d5.print_grade()
print ""

print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. UpgradeCalculator"
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value = self.value + val
        return self.value

class UpgradeCalculator(Calculator):
    def sub(self, val):
        self.value = self.value - val
        return self.value

cal = UpgradeCalculator()
print cal.add(10)
print cal.sub(7)
print ""

print "2. MaxLimitCalculator"
class MaxLimitCalculator(UpgradeCalculator):
    def add(self, val):
        if self.value + val > 100:
            print "You can not add more than 100."
            self.value = self.value
            return self.value
        else:
            self.value = self.value + val
            return self.value
cal = MaxLimitCalculator()
print cal.add(50)
print cal.add(50)
print cal.add(1)

#!/usr/bin/env python
#-*- encoding: utf-8


def add(a, b):
    return a + b


print add(3, 4)
print ""


def say():
    return "Hi"


print say()
print ""


def add2(a, b):
    print "%d, %d의 합은 %d 입니다." % (a, b, a + b)


add2(3, 4)
print ""


def say2():
    print "say 2 Hi"


say2()
print ""


def add_many(*args):
    res = 0
    for i in args:
        res = res + i
    return res


print add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print add_many(1, 2, 3, 4, 5)
print ""


def add_mul(choice, *args):
    if choice == "add":
        res = 0
        for i in args:
            res = res + i
    elif choice == "mul":
        res = 1
        for i in args:
            res = res * i
    else:
        res = "잘못된 choice 입력"
    return res


print add_mul("add", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print add_mul("mul", 1, 2, 3, 4, 5)
print add_mul("sub", 1, 2, 3)
print ""


def print_kwargs(**kwargs):
    print kwargs


print_kwargs(a=1)
print_kwargs(name="wooneo", what="wedding", withWho="jenna")


def add_and_mul(a, b):
    return a + b, a * b


res = add_and_mul(3, 4)
print res
print type(res)
print res[0]
print res[1]
# res[1] = 15 -- ERROR why res is tuple
print ""


# 초기화시키고 싶은 매개변수들을 항상 뒤쪽에 위치시키는 것을 잊지 말자.
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("wooneo", 31)
say_myself("jenna", 30, False)
print ""


lambda_add = lambda a, b: a + b
res = lambda_add(3, 4)
print res
print ""


# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 홀수 짝수 판별"
def is_odd(n):
    if n % 2 == 1:
        print "홀수"
    else:
        print "짝수"
"1 = " + str(is_odd(1))
"2 = " + str(is_odd(2))
"3 = " + str(is_odd(3))
"4 = " + str(is_odd(4))
"5 = " + str(is_odd(5))
print "2. 평균값 계산"
def avg_calc(*args):
    s = 0.0
    cnt = 0
    for i in args:
        cnt = cnt + 1
        s = s + i
    avg = s / cnt
    return avg
print "1, 2, 3 의 평균은 " + str(avg_calc(1, 2, 3))
print "1, 2, 3, 4, 5 의 평균은 " + str(avg_calc(1, 2, 3, 4, 5))
print "1, 2, 3, 4 의 평균은 " + str(avg_calc(1, 2, 3, 4))

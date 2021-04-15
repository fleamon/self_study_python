#-*- encoding: utf-8

a = input("입력숫자 : ")
print "입력숫자는 %d 입니다." % a
print""

b = raw_input("입력문자 : ")
# print "입력문자는 %d 입니다." % b -- ERROR %d = 숫자
print "입력문자는 %s 입니다." % b
print ""

# 연습문제
print "=" * 30
print "연습문제!!!!!"
print "=" * 30
print "1. 두 수의 합은?"
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
# input 대신 raw_input 을 쓰면 문자 두개가 결합된다.
total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
print ""
print "2. 숫자의 총합"
a = input("숫자여러개 입력 : ")
res = 0
for i in a:
    res = res + i
print "입력한 숫자 여러개의 합은 " + str(res) + "입니다."
print ""
print "3. 문자열 출력"
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print "you", "need", "python"
print("".join(["you", "need", "python"]))
print ""
print "4. 한줄 구구단"
a = input("몇단할까요? : ")
res = ""
for i in range(1, 10):
    res = res + str(a * i) + " "
print res

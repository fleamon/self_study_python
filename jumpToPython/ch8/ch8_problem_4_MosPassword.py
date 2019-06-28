#!/usr/bin/env python
# -*- encoding: utf-8

"""
문자열 형식으로 입력받은 모스 부호(dot: . dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성해 보자.
글자와 글자 사이는 공백 하나, 단어와 단어 사이는 공백 두개로 구분한다.

입력 : .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
출력 : HE SLEEPS EARLY

문자	부호	문자	부호
A	.-	    N	-.
B	-...	O	---
C	-.-.	P	.--.
D	-..	    Q	--.-
E	.	    R	.-.
F	..-.	S	...
G	--.	    T	-
H	....	U	..-
I	..	    V	...-
J	.---	W	.--
K	-.-	    X	-..-
L	.-..	Y	-.--
M	--	    Z	--..
"""

mos = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
       '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'N', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
       '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
def MosPassword(s):
    res = []
    words = s.split("  ")
    cnt = 0
    # print len(words)
    for word in words:
        # print word
        alphabet = word.split()
        for i in alphabet:
            # print i
            res.append(mos[i])
            # print mos[i]
        cnt = cnt + 1
        if cnt < len(words):
            res.append(" ")
        # print cnt
    print res
    return "".join(res)


inputStr = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
print MosPassword(inputStr)

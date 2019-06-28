#!/usr/bin/env python
# -*- encoding: utf-8

"""
0~9까지의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9까지의 모든 숫자가 각각 한 번씩만 사용된 것인지 확인하는 함수를 작성해 보자.

입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: true false false true false
"""

def dupNum(s):
    res = []
    outputStr = s.split()
    # print len(outputStr)  # print input param's length
    # print ""
    # print ""
    # print ""
    for i in range(0, len(outputStr)):
        tmpD = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for j in outputStr[i]:
            # print j  # print input param's digit
            try:
                tmpD[j] = tmpD[j] + 1
            except:
                pass
        # print outputStr[i]  # print input param
        # print ""
        # print len(tmpD)
        cnt = 0
        for i in tmpD:
            if tmpD[i] != 1:
               cnt = cnt + 1
        if cnt == 0:
            res.append("true")
        else:
            res.append("false")
    # print tmpD
    # return res
    return ", ".join(res)
    # return tmpD

# inputStr = raw_input("문자열 입력 : ")
inputStr = "0123456789 01234 01234567890 6789012345 012322456789"
# inputStr = "01234"
print dupNum(inputStr)

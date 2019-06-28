#!/usr/bin/env python
# -*- encoding: utf-8

"""
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
"""

def strZip(s):
    res = []
    tmp = ""
    chArr = []
    cntArr = []
    for i in range(0, len(s)):
        if tmp != s[i]:
            if len(res) > 1:
               cntArr.append(res[len(res) - 1])
            tmp = s[i]
            chArr.append(tmp)
            res.append(tmp)
            cnt = 0
        cnt = cnt + 1
        res.append(cnt)
    cntArr.append(cnt)

    result = []
    for i in range(0, len(cntArr)):
        result.append(chArr[i])
        result.append(str(cntArr[i]))
    #return result
    return "".join(result)


inputStr = raw_input("문자열입력 : ")
# inputStr = "aaabbcccccca"
print strZip(inputStr)

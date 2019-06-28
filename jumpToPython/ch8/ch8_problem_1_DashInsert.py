#!/usr/bin/env python
# -*- encoding: utf-8

import sys

def dashInsert(str):
    res = []
    lenStr = len(str) - 1
    for i in range(0, lenStr):
        if str[i].isdigit() and str[i + 1].isdigit():
            res.append(str[i])
            if int(str[i]) % 2 == 0 and int(str[i + 1]) % 2 == 1:
                pass
            elif int(str[i]) % 2 == 0 and int(str[i + 1]) % 2 == 0:
                res.append("*")
            elif int(str[i]) % 2 == 1 and int(str[i + 1]) % 2 == 1:
                res.append("-")
            elif int(str[i]) % 2 == 1 and int(str[i + 1]) % 2 == 0:
                pass
        else:
            sys.exit(1)
    res.append(str[lenStr])
    return "".join(res)
    # return str


inputStr = dashInsert(raw_input("문자열입력 : "))
print inputStr

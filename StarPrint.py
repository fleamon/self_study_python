#!/usr/bin/env python
# -*- encoding: utf-8

n = input("몇 줄? : ")
maxLen = n * 2 - 1

for i in range(1, n+1):
    starCnt = i * 2 - 1
    spaceCnt = (maxLen - starCnt) / 2
    print (" " * spaceCnt) + ("*" * starCnt)

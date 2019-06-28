#!/usr/bin/env python
# -*- encoding: utf-8


def gugudan(n):
    res = []
    for i in range(1, 10):
        print str(n) + " * " + str(i) + " = " + str(n * i)
        res.append(n * i)
    print res


gugudan(input("몇단?"))

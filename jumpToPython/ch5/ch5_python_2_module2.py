#!/usr/bin/env python
#-*- encoding: utf-8

"""
import ch5_python_2_module
ch5_python_2_module.add(1, 2)
"""

from ch5_python_2_module import add
print add(1, 2)
print ""

from ch5_python_2_module import sub
print sub(2, 1)
print""

from ch5_python_2_module import *
print add(2, 3)
print sub(10, 3)
print ""

PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r ** 2)

print "=" * 30
print "연습문제!!!!!"
print "=" * 30

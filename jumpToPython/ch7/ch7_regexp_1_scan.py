#!/usr/bin/env python
# -*- encoding: utf-8

data = """
park 800905-1049118
kim  700905-1059119
"""

print "방법1"
res = []
for line in data.split("\n"):
    if line.split("-")[0] != "":
        print line.split("-")[0] + "-" + line.split("-")[1].replace(line.split("-")[1], "*******")
print ""
print ""
print ""
print ""
print ""



print "방법2"
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
print ""
print ""
print ""
print ""
print ""



print "방법3"
import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


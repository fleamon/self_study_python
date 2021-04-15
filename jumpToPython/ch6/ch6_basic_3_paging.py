# -*- encoding: utf-8


def getPageCount(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print getPageCount(5, 10)
print getPageCount(15, 10)
print getPageCount(25, 10)
print getPageCount(30, 10)

# -*- encoding: utf-8

import time


def cnt_prime(n):
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k * 2::k] = [False] * ((n - k) // k)
    return [x for x in range(n + 1) if seive[x]]


start_time = time.time()
print "count : " + str(len(cnt_prime(2000000)))
end_time = time.time()

print "timing on : {} sec".format(end_time - start_time)

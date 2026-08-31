"""https://projecteuler.net/problem=16
"""

import time
import Commons

if __name__=='__main__':
    t = time.time()
    Commons.digitsum(2**1_000_000)
    print(time.time() - t)
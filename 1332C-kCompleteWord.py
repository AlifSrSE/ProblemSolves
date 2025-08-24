# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from collections import Counter

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        changes = 0
        
        for p in range(k // 2):
            tally = Counter()

            for i in range(p, n, k):
                tally[s[i]] += 1

            for i in range(k - 1 - p, n, k):
                tally[s[i]] += 1
            group_size = (n // k) * 2
            max_freq = max(tally.values())
            changes += (group_size - max_freq)
        
        if k % 2 != 0:
            p = k // 2
            tally = Counter()

            for i in range(p, n, k):
                tally[s[i]] += 1
            group_size = n // k
            max_freq = max(tally.values())
            changes += (group_size - max_freq)
        
        sys.stdout.write(str(changes) + "\n")
        t -= 1

alif()
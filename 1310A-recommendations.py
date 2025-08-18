# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1310/problem/A

import sys
import collections
import heapq

def alif():
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))
    t = list(map(int, sys.stdin.readline().split()))

    d = collections.defaultdict(list)
    for p in range(n):
        d[v[p]].append(t[p])

    w = sorted(d.keys())

    carry = []
    cur_sum = 0
    res = 0
    
    for p in range(len(w)):
        key = w[p]
        
        while carry and (p + 1 == len(w) or w[p + 1] > key + 1):
            res += cur_sum
            item = -heapq.heappop(carry)
            cur_sum -= item
            key += 1
        
        for item in d[key]:
            heapq.heappush(carry, -item)
            cur_sum += item
        
    while carry:
        res += cur_sum
        item = -heapq.heappop(carry)
        cur_sum -= item

    print(res)

if __name__ == "__main__":
    alif()
# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2037/B

import sys
import math
from collections import Counter

def solve(k, a):
    m = Counter(a) 
    v = k - 2
    sqrt_v = int(math.sqrt(v))  
    possible_divisors = set(m.keys()) & set(range(1, sqrt_v + 1))

    for i in possible_divisors:
        if v % i == 0:
            vv = v // i

            if vv in m:
                print(i, vv)
                return
            elif i == vv and m[i] >= 2:
                print(i, vv)
                return

input = sys.stdin.read
data = input().split()
t = int(data[0])

index = 1
results = []
for _ in range(t):
    k = int(data[index])
    a = list(map(int, data[index + 1 : index + 1 + k]))
    solve(k, a)
    index += 1 + k

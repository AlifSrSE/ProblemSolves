# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# https://codeforces.com/problemset/problem/2096/F

import sys
input = sys.stdin.readline

def process():
    n, m = map(int, input().split())
    statements = []
    for _ in range(m):
        x, a, b = map(int, input().split())
        mask = 0
        for i in range(a - 1, b):
            mask |= 1 << i
        statements.append((x, mask))
    
    q = int(input())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l - 1, r - 1))
    
    for l_q, r_q in queries:
        relevant = statements[l_q : r_q + 1]
        possible = False
        for i in range(1 << n):
            valid = True
            for x, mask in relevant:
                impostors = (i & mask).bit_count()
                if x == 0 and impostors > 0:
                    valid = False
                    break
                if x == 1 and impostors == 0:
                    valid = False
                    break
            if valid:
                possible = True
                break
        print("YES" if possible else "NO")

t = int(input())
for _ in range(t):
    process()
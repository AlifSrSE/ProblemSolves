# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1218/problem/F

import heapq

def alif():
    n, cur = map(int, input().split())
    w = list(map(int, input().split()))
    a = int(input())
    d = list(map(int, input().split()))
    cost = 0
    possible = True
    s = []

    for p in range(n):
        heapq.heappush(s, d[p])
        while s and cur < w[p]:
            cur += a
            cost += heapq.heappop(s)
        if cur < w[p]:
            possible = False
            break 
    if possible:
        print(cost)
    else:
        print("-1")

if __name__ == "__main__":
    alif()
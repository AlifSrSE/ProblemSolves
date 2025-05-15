# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1174/problem/B

import heapq

def alif(a):
    evens = []
    odds = []

    for ai in a:
        if ai % 2 == 0:
            heapq.heappush(evens, ai)
        else:
            heapq.heappush(odds, ai)

    if not evens or not odds:
        return a

    result = []
    for _ in range(len(a)):
        if not odds or (evens and evens[0] < odds[0]):
            result.append(heapq.heappop(evens))
        else:
            result.append(heapq.heappop(odds))
    return result

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(" ".join(map(str, alif(a))))

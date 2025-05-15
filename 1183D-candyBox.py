# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1183/problem/D

from collections import Counter

def alif(a):
    value_to_count = Counter(a)
    counts = sorted(value_to_count.values(), reverse=True)
    result = 0
    limit = float('inf')
    for count in counts:
        chosen = min(limit, count)
        result += chosen
        limit = max(0, chosen - 1)
    return result

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(alif(a))

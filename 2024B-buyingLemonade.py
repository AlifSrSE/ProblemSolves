# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    result = 0
    for i in range(n):
        if i != 0:
            result += 1

        diff = (a[i] - (a[i - 1] if i > 0 else 0)) * (n - i)
        if diff >= k:
            result += k
            return result

        result += diff
        k -= diff
    return result

t = int(input())
for _ in range(t):
    print(solve())
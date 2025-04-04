# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    s = sorted(input())

    sum_val = ord(s[0]) - ord('a') + 1
    k -= 1
    prev = s[0]

    for i in range(1, n):
        if k == 0:
            break
        if ord(s[i]) - ord(prev) >= 2:
            prev = s[i]
            sum_val += ord(s[i]) - ord('a') + 1
            k -= 1

    if k == 0:
        print(sum_val)
        return
    print(-1)

solve()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif(n, t):
    if len(set(t)) == 1:
        return 1, [1] * n
    k = 2
    c = [0] * n
    c[0] = 1
    for i in range(1, n):
        c[i] = 3 - c[i-1] if t[i] != t[i-1] else c[i-1]
    if t[0] != t[n-1] and c[0] == c[n-1]:
        for i in range(n):
            if i > 0 and t[i] != t[i-1] and c[i] == c[i-1]:
                c[i] = 3
                k = 3
                break
            if i < n-1 and t[i] != t[i+1] and c[i] == c[(i+1)%n]:
                c[i] = 3
                k = 3
                break
    return k, c

q = int(input())
for _ in range(q):
    n = int(input())
    t = list(map(int, input().split()))
    k, c = alif(n, t)
    print(k)
    print(*c)
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif():
    n, k = map(int, input().split())
    s = list(input())

    last_one = -k - 1
    for i in range(n):
        if s[i] == '1':
            last_one = i
        elif i - last_one <= k:
            s[i] = 'x'

    count = 0
    last_one = n + k + 1
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            last_one = i
        elif s[i] == '0' and last_one - i > k:
            count += 1
            last_one = i

    print(count)

t = int(input())
for _ in range(t):
    alif()
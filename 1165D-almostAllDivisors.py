# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1165/problem/D

def alif(d):
    d.sort()
    
    number = d[0] * d[-1]
    i, j = 0, len(d) - 1
    while i <= j:
        if d[i] * d[j] != number:
            return -1
        i += 1
        j -= 1
    
    count = 0
    i = 2
    while i * i <= number:
        if number % i == 0:
            count += 1
        i += 1
    
    if (len(d) + 1) // 2 != count:
        return -1
    
    return number

t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print(alif(d))
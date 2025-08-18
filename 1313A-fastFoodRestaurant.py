# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1313/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        counts = [a, b, c]
        counts.sort(reverse=True)
        a, b, c = counts[0], counts[1], counts[2]
        count = 0
        
        if a > 0:
            count += 1
            a -= 1
        if b > 0:
            count += 1
            b -= 1
        if c > 0:
            count += 1
            c -= 1
        if a > 0 and b > 0:
            count += 1
            a -= 1
            b -= 1
        if a > 0 and c > 0:
            count += 1
            a -= 1
            c -= 1
        if b > 0 and c > 0:
            count += 1
            b -= 1
            c -= 1
        if a > 0 and b > 0 and c > 0:
            count += 1
            a -= 1
            b -= 1
            c -= 1
        print(count)

alif()
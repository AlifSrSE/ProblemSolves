# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1315/problem/B

def alif():
    t = int(input())
    for _ in range(t):
        a, b, p = map(int, input().split())
        s = input()
        n = len(s)
        cost = 0
        ans = n
        
        for i in range(n - 2, -1, -1):
            if s[i] != s[i + 1]:
                if s[i + 1] == 'A':
                    cost += a
                else:
                    cost += b
            
            if cost <= p:
                ans = i + 2
            else:
                break
        
        print(ans)

alif()
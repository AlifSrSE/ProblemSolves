# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1200/problem/B

def alif():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prev = int(input())
        possible = True
        
        for p in range(1, n):
            x = int(input())
            
            if prev + m + k < x:
                possible = False
            else:
                m -= (max(0, x - k) - prev)
            
            prev = x
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/D

from sys import stdin
input = stdin.readline

def checker(s):
    return s[0] == s[4] and s[1] == s[3]

def main():
    t = int(input().strip()) 
    
    for _ in range(t):
        s, x = input().strip().split()
        x = int(x)
        
        ch = int(s[0:2])
        cm = int(s[3:5])
        
        cnt = 0
        seen = set()
        
        for i in range(1500):
            minutes = x * (i + 1)
            h = minutes // 60
            m = minutes % 60
            
            new_m = (cm + m) % 60
            new_h = (ch + (cm + m) // 60 + h) % 24
            ans = f"{new_h:02d}:{new_m:02d}"
            
            if checker(ans) and ans not in seen:
                seen.add(ans)
                cnt += 1
        
        print(cnt)

if __name__ == "__main__":
    main()
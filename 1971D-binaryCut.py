# Author: AlifSrSe
# date: 2025-03-19
# https://codeforces.com/problemset/problem/1971/D

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        cnt = 0 
        f = 0    
        
        i = 0
        while i < n:
            if s[i] == '1':
                while i < n and s[i] == '1':
                    i += 1
                cnt += 1
            elif s[i] == '0':
                while i < n and s[i] == '0':
                    i += 1
                cnt += 1
                if i < n and s[i] == '1':
                    f = 1
        
        if f:
            cnt -= 1
            
        print(cnt)

if __name__ == "__main__":
    main()
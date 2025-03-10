# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1941/problem/C

def main():
    TC = int(input())
    for _ in range(TC):
        n = int(input())
        s = input()       

        res = 0
        for i in range(2, n):
            if s[i-2] == 'p' and s[i-1] == 'i' and s[i] == 'e':
                res += 1
        
        for i in range(2, n):
            if s[i-2] == 'm' and s[i-1] == 'a' and s[i] == 'p':
                res += 1

        for i in range(4, n):
            if (s[i-4] == 'm' and s[i-3] == 'a' and s[i-2] == 'p' and 
                s[i-1] == 'i' and s[i] == 'e'):
                res -= 1
        
        print(res)

if __name__ == "__main__":
    main()
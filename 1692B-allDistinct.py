# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/B

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip()) 
    
    for _ in range(t):
        n = int(input().strip())
        a = set(map(int, input().strip().split()))
        ans = len(a)
        rem = n - len(a)
        if rem % 2:
            ans -= 1
            
        print(ans)

if __name__ == "__main__":
    main()
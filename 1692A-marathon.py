# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/A

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip())
    
    for _ in range(t):
        a, b, c, d = map(int, input().strip().split())
        result = sum(1 for x in (b, c, d) if x > a)
        
        print(result)

if __name__ == "__main__":
    main()
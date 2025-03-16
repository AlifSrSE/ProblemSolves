# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/B
 
def solve():
    n, k = map(int, input().split())
    if k % 2 == 1: 
        for i in range(1, n):
            print(n, end=" ")
        print(n-1)
    else:
        for i in range(1, n-1):
            print(n-1, end=" ")
        print(n, n-1)
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
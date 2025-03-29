# Author : AlifSrSE
# Date : 2025-03-29
# Problem link : https://codeforces.com/contest/2071/problem/A

def solve():
    n = int(input())
    if n % 3 == 1:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
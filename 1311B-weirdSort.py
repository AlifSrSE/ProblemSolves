# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1311/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        p = list(map(int, sys.stdin.readline().split()))

        b = [False] * n
        for pos in p:
            b[pos - 1] = True

        for i in range(n):
            j = i
            while j < n - 1 and b[j]:
                j += 1
            if j > i:
                a[i:j+1] = sorted(a[i:j+1])
            i = j

        is_sorted = True
        for i in range(n - 1):
            if a[i] > a[i+1]:
                is_sorted = False
                break
        
        if is_sorted:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()
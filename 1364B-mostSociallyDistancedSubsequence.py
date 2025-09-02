# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    ans = []
    
    if n > 0:
        ans.append(a[0])
    
    for p in range(1, n - 1):
        if (a[p - 1] < a[p] and a[p] > a[p + 1]) or (a[p - 1] > a[p] and a[p] < a[p + 1]):
            ans.append(a[p])
    
    if n > 1:
        ans.append(a[n - 1])

    sys.stdout.write(f"{len(ans)}\n")
    sys.stdout.write(" ".join(map(str, ans)) + "\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

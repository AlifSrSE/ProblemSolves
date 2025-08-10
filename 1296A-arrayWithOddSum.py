# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1296/problem/A

import sys

def alif():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        numbers = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    has_odd = any(x % 2 != 0 for x in numbers)
    
    if has_odd:
        print("YES")
    else:
        print("NO")

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
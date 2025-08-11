# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1301/problem/A

import sys

def solve():
    try:
        a = sys.stdin.readline().strip()
        b = sys.stdin.readline().strip()
        c = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return
    
    is_possible = True
    for i in range(len(a)):
        if not (a[i] == c[i] or b[i] == c[i]):
            is_possible = False
            break

    if is_possible:
        print("YES")
    else:
        print("NO")

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
    except (IOError, ValueError):
        return
        
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
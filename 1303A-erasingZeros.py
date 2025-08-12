# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1303/problem/A

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            s = sys.stdin.readline().strip()
            if not s:
                continue
        except (IOError, ValueError):
            continue
        try:
            first_one = s.index('1')
            last_one = s.rindex('1')
        except ValueError:
            print(0)
            continue
        
        substring = s[first_one:last_one + 1]
        cnt = substring.count('0')
        print(cnt)

if __name__ == "__main__":
    alif()
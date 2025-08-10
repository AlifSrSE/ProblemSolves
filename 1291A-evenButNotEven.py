# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1291/problem/A

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    while t > 0:
        try:
            n = int(sys.stdin.readline())
            s = sys.stdin.readline().strip()
        except (IOError, ValueError):
            t -= 1
            continue

        cnt = 0
        for char in s:
            if int(char) % 2 != 0:
                cnt += 1
        
        if cnt < 2:
            print("-1")
            t -= 1
            continue

        cnt_mod_2 = cnt % 2
        pos = n - 1

        for p in range(n - 1, -1, -1):
            if int(s[p]) % 2 == 0:
                continue
            
            if cnt_mod_2 == 1:
                cnt_mod_2 = 0
            else:
                pos = p
                break
        
        print(s[:pos + 1])
        
        t -= 1

if __name__ == "__main__":
    alif()
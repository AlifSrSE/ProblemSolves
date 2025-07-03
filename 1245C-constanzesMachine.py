# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1245/problem/C

import sys

def alif():
    MOD = 10**9 + 7
    MAX_LEN = 100000 + 7
    f = [0] * MAX_LEN
    f[0] = 1
    f[1] = 1
    f[2] = 2
    for p in range(3, MAX_LEN):
        f[p] = (f[p - 1] + f[p - 2]) % MOD

    s = sys.stdin.readline().strip()
    cnt = 1
    tmp = 0

    for p in range(len(s)):
        if s[p] == 'm' or s[p] == 'w':
            cnt = 0
            break

        elif s[p] == 'u':
            tmp += 1
            if p + 1 == len(s) or s[p + 1] != 'u':
                cnt = (cnt * f[tmp]) % MOD
                tmp = 0
        
        elif s[p] == 'n':
            tmp += 1
            if p + 1 == len(s) or s[p + 1] != 'n':
                cnt = (cnt * f[tmp]) % MOD
                tmp = 0
        
        else:
            pass

    sys.stdout.write(f"{cnt}\n")
if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1278/A

import sys

def all_zeros(v):
    for val in v:
        if val != 0:
            return False
    return True

def alif():
    N_ALPHABET = 26
    t = int(sys.stdin.readline())

    for _ in range(t):
        s = sys.stdin.readline().strip()
        r = sys.stdin.readline().strip()
        f = [0] * N_ALPHABET

        for char_s in s:
            f[ord(char_s) - ord('a')] += 1
            
        if len(r) < len(s):
            sys.stdout.write("NO\n")
            continue
        
        for p in range(len(s)):
            f[ord(r[p]) - ord('a')] -= 1
            
        if all_zeros(f):
            sys.stdout.write("YES\n")
            continue
        
        ans = False

        for p in range(len(s), len(r)):
            f[ord(r[p - len(s)]) - ord('a')] += 1
            f[ord(r[p]) - ord('a')] -= 1

            if all_zeros(f):
                ans = True
                break
        sys.stdout.write("YES\n" if ans else "NO\n")

if __name__ == "__main__":
    alif()
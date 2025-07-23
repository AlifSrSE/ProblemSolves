# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1251/problem/A

import sys

def alif():
    N_ALPHA = 26
    q = int(sys.stdin.readline())

    for _ in range(q):
        s = sys.stdin.readline().strip()
        w = [0] * N_ALPHA 
        cnt = 1
        
        for p in range(1, len(s)):
            if s[p] == s[p - 1]:
                cnt += 1
            else:
                char_idx = ord(s[p - 1]) - ord('a')
                w[char_idx] |= (cnt % 2)
                
                cnt = 1
        char_idx_last = ord(s[-1]) - ord('a')
        w[char_idx_last] |= (cnt % 2)
        result_chars = []

        for p in range(N_ALPHA):
            if w[p] == 1:
                result_chars.append(chr(ord('a') + p))
        
        sys.stdout.write("".join(result_chars) + "\n")

if __name__ == "__main__":
    alif()
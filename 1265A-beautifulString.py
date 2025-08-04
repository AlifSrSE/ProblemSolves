# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1265/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s_list = list(sys.stdin.readline().strip())
        
        possible = True
        
        for p in range(len(s_list)):
            if s_list[p] != '?':
                if p > 0 and s_list[p - 1] == s_list[p]:
                    possible = False
                    break
                else:
                    continue
                
            for q in range(3):
                cand = chr(ord('a') + q)

                if p > 0 and cand == s_list[p - 1]:
                    continue
                
                if p + 1 < len(s_list) and cand == s_list[p + 1]:
                    continue
                s_list[p] = cand
                break
        
        if possible:
            sys.stdout.write("".join(s_list) + "\n")
        else:
            sys.stdout.write("-1\n")

if __name__ == "__main__":
    alif()
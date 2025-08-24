# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        s += 'R'
        max_jump = 0
        last_r_index = -1
        
        for i in range(len(s)):
            if s[i] == 'R':
                diff = i - last_r_index
                max_jump = max(max_jump, diff)
                last_r_index = i
        
        print(max_jump)
alif()
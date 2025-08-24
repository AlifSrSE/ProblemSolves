# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n, a, b = map(int, sys.stdin.readline().split())
        result_list = []

        for p in range(n):
            char_code = ord('a') + (p % b)
            result_list.append(chr(char_code))
        
        result_string = "".join(result_list)
        sys.stdout.write(result_string + '\n')
        t -= 1

alif()
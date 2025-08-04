# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1266/A

import sys

def alif():
    n_test_cases = int(sys.stdin.readline())

    for _ in range(n_test_cases):
        s = sys.stdin.readline().strip()
        v_flag = False
        z_flag = False
        total_sum_digits = 0
        
        for char_digit in s:
            d = int(char_digit)
            total_sum_digits += d
            
            if d == 0 and not z_flag:
                z_flag = True
            elif d % 2 == 0:
                v_flag = True
        
        ans_is_red = (z_flag and v_flag and (total_sum_digits % 3 == 0)) or (s == "0")
        sys.stdout.write("red\n" if ans_is_red else "cyan\n")

if __name__ == "__main__":
    alif()
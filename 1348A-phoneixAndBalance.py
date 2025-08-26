# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n = int(sys.stdin.readline())
        except (IOError, ValueError):
            continue

        pile_a_sum = 0
        pile_b_sum = 0
        pile_a_sum += 2**n
        
        for i in range(n - 1, n // 2, -1):
            pile_b_sum += 2**i
            
        for i in range(1, n // 2 + 1):
            pile_a_sum += 2**i
            
        pile_a_sum = 0
        pile_b_sum = 0
        pile_a_sum += 2**n
        for i in range(1, n // 2):
            pile_a_sum += 2**i
            
        for i in range(n // 2, n):
            pile_b_sum += 2**i
            
        diff = abs(pile_a_sum - pile_b_sum)
        
        print(diff)

if __name__ == "__main__":
    alif()
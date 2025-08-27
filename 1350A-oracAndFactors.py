# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        def find_smallest_divisor(num):
            if num % 2 == 0:
                return 2
            
            d = 3
            while d * d <= num:
                if num % d == 0:
                    return d
                d += 2
            return num
        
        d = find_smallest_divisor(n)
        result = n + d + 2 * (k - 1)
        print(result)

if __name__ == "__main__":
    alif()
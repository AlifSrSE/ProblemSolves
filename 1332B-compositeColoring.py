# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        
        color_map = {}
        next_color = 1
        result = [0] * n
        
        for i in range(n):
            for prime in primes:
                if a[i] % prime == 0:
                    if prime not in color_map:
                        color_map[prime] = next_color
                        next_color += 1
                    result[i] = color_map[prime]
                    break
        
        print(next_color - 1)
        print(*result)

alif()
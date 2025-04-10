# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def main():
    s = set()
    max_p_square = int(math.isqrt(10**9)) + 1
    for p in range(1, max_p_square):
        s.add(p * p)
    max_p_cube = int(round((10**9) ** (1/3))) + 1
    for p in range(1, max_p_cube):
        s.add(p * p * p)
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for num in sorted(s):
            if num <= n:
                cnt += 1
            else:
                break
        print(cnt)

if __name__ == "__main__":
    main()
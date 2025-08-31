# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    a, b, c, d = map(int, sys.stdin.readline().split())
    ans = 0
    for z in range(c, d + 1):
        min_x = max(a, z - c + 1)
        if min_x > b:
            continue

        min_y = z - b
        max_y = z - min_x
        lower_bound = max(min_x, z - c)
        upper_bound = min(b, z - b)
        if lower_bound <= upper_bound:
            ans += (upper_bound - lower_bound) + 1
            
    print(ans)

def main():
    alif()

if __name__ == "__main__":
    main()
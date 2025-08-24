# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        max_so_far = a[0]
        max_diff = 0

        for i in range(1, n):
            if a[i] > max_so_far:
                max_so_far = a[i]
            else:
                current_diff = max_so_far - a[i]
                max_diff = max(max_diff, current_diff)
        
        k = 0
        if max_diff > 0:
            temp_diff = max_diff
            while temp_diff > 0:
                temp_diff //= 2
                k += 1

        print(k)

if __name__ == "__main__":
    alif()
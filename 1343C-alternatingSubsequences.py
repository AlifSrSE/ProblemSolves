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
        
        try:
            a = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            continue

        if not a:
            print(0)
            continue

        total_sum = 0
        current_num = a[0]
        
        for i in range(1, n):
            if a[i] * current_num > 0:
                current_num = max(current_num, a[i])
            else:
                total_sum += current_num
                current_num = a[i]

        total_sum += current_num
        print(total_sum)

if __name__ == "__main__":
    alif()
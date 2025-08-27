# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().strip().split()))
        special_sums = set()

        for i in range(n):
            current_sum = a[i]
            for j in range(i + 1, n):
                current_sum += a[j]
                special_sums.add(current_sum)

        count = 0
        for element in a:
            if element in special_sums:
                count += 1
        
        print(count)

if __name__ == "__main__":
    alif()
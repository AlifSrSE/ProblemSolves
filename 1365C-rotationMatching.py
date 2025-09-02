# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    
    a_pos = [0] * (n + 1)
    for i in range(n):
        a_pos[a_list[i]] = i
    
    b_pos = [0] * (n + 1)
    for i in range(n):
        b_pos[b_list[i]] = i
    
    shifts = [0] * n
    
    for i in range(1, n + 1):
        shift = b_pos[i] - a_pos[i]
        if shift < 0:
            shift += n
        shifts[shift] += 1
    
    max_count = 0
    if shifts:
        max_count = max(shifts)
    
    sys.stdout.write(str(max_count) + "\n")

if __name__ == "__main__":
    alif()

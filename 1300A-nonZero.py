# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1300/problem/A

import sys

def solve():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
    num_zeros = 0
    total_sum = 0

    for x in a:
        if x == 0:
            num_zeros += 1
        total_sum += x
    
    operations = num_zeros
    new_sum = total_sum + num_zeros
    if new_sum == 0:
        operations += 1
    print(operations)

def main():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().split())
        
        if b >= a:
            print(b)
        elif c <= d:
            print(-1)
        else:
            remaining_sleep_needed = a - b
            sleep_per_cycle = c - d
            cycles = (remaining_sleep_needed + sleep_per_cycle - 1) // sleep_per_cycle
            total_time = b + cycles * c
            print(total_time)

if __name__ == "__main__":
    main()
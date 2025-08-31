# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    count = 0
    current_group_size = 0
    
    for val in a:
        current_group_size += 1
        if current_group_size >= val:
            count += 1
            current_group_size = 0
    print(count)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
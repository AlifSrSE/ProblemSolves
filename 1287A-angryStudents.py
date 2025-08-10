# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1287/problem/A

import sys

def alif():
    try:
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return

    last_a_index = -1
    max_time = 0
    
    for i, char in enumerate(s):
        if char == 'A':
            last_a_index = i

        elif char == 'P':
            if last_a_index != -1:
                current_time = i - last_a_index
                max_time = max(max_time, current_time)
    print(max_time)

def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            alif()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
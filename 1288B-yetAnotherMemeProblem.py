# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1288/problem/B

import sys

def alif():
    try:
        a, b = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return
    
    count_b = 0
    current_b = 9
    
    while current_b <= b:
        count_b += 1
        current_b = current_b * 10 + 9
        
    result = a * count_b
    print(result)

def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            alif()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
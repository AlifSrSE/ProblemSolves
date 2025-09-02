# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    odd_count = sum(1 for num in a if num % 2 != 0)
    even_count = n - odd_count
    
    possible = False
    for i in range(1, min(odd_count, x) + 1, 2):
        if x - i <= even_count:
            possible = True
            break
            
    if possible:
        print("Yes")
    else:
        print("No")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

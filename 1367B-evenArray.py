# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    wrong_even = 0
    wrong_odd = 0
    
    for i in range(n):
        if i % 2 != a[i] % 2:
            if i % 2 == 0:
                wrong_even += 1
            else:
                wrong_odd += 1
    
    if wrong_even == wrong_odd:
        sys.stdout.write(str(wrong_even) + "\n")
    else:
        sys.stdout.write("-1\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
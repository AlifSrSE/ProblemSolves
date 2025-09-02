# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    is_sorted = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            is_sorted = False
            break

    has_zero = 0 in b
    has_one = 1 in b

    if is_sorted or (has_zero and has_one):
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

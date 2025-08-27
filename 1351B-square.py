# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        c, d = map(int, sys.stdin.readline().split())

        if a == c and b + d == a:
            print("Yes")
        elif a == d and b + c == a:
            print("Yes")
        elif b == c and a + d == b:
            print("Yes")
        elif b == d and a + c == b:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())

        if (n - (k - 1)) > 0 and (n - (k - 1)) % 2 == 1:
            print("YES")
            for _ in range(k - 1):
                print(1, end=" ")
            print(n - (k - 1))
        
        elif (n - 2 * (k - 1)) > 0 and (n - 2 * (k - 1)) % 2 == 0:
            print("YES")
            for _ in range(k - 1):
                print(2, end=" ")
            print(n - 2 * (k - 1))
        else:
            print("NO")

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n = int(sys.stdin.readline())
        except (IOError, ValueError):
            continue

        if n % 4 != 0:
            print("NO")
            continue
        
        print("YES")
        result = []

        for i in range(1, n // 2 + 1):
            result.append(2 * i)
        
        for i in range(1, n // 2):
            result.append(2 * i - 1)

        result.append(3 * n // 2 - 1)
        print(*result)

if __name__ == "__main__":
    alif()
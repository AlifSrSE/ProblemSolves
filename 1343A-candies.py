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
        
        p = 2
        while True:
            divisor = (1 << p) - 1
            
            if n % divisor == 0:
                print(n // divisor)
                break
            
            p += 1

if __name__ == "__main__":
    alif()
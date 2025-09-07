# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(sys.stdin.readline())
    div = n
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            div = p
            break
    
    print(n // div, n - (n // div))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

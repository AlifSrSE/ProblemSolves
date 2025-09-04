# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    a, b, n = map(int, sys.stdin.readline().split())
    
    count = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        count += 1
    
    sys.stdout.write(str(count) + '\n')

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == '__main__':
    main()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    while t > 0:
        n = int(sys.stdin.readline())
        print(n // 2)
        t -= 1

if __name__ == '__main__':
    main()

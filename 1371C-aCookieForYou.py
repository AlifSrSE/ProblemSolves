# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, n, m = map(int, sys.stdin.readline().split())
        
        if m + n <= a + b and m <= min(a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

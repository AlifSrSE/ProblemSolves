# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    x, y, n = map(int, sys.stdin.readline().split())
    ans = n - (n % x) + y

    if ans > n:
        ans -= x
    print(ans)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

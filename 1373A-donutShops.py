# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def solve():
    a, b, c = map(int, sys.stdin.readline().split())
    if a < c:
        x = 1
    else:
        x = -1
        
    if a * b > c:
        y = b
    else:
        y = -1

    print(x, y)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n, k = map(int, sys.stdin.readline().split())
    grid = [['0'] * n for _ in range(n)]
    
    for i in range(k):
        row = i % n
        col = (i // n + i % n) % n
        grid[row][col] = '1'
    
    if k % n == 0:
        print(0)
    else:
        print(1)
    
    for row in grid:
        print("".join(row))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == '__main__':
    main()

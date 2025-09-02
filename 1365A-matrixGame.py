# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, m = map(int, sys.stdin.readline().split())
    rows = [True] * n
    cols = [True] * m
    for row in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for col in range(m):
            if line[col] == 1:
                rows[row] = False
                cols[col] = False
    
    u = sum(rows)
    v = sum(cols)
    turns = min(u, v)
    
    if turns % 2 == 1:
        sys.stdout.write("Ashish\n")
    else:
        sys.stdout.write("Vivek\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

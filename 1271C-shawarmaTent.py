# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1271/C

import sys

def alif():
    n, sx, sy = map(int, sys.stdin.readline().split())
    under = 0
    above = 0
    left = 0
    right = 0
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if y < sy:
            under += 1
        elif y > sy:
            above += 1
        
        if x < sx:
            left += 1
        elif x > sx:
            right += 1
    
    if under >= above and under >= left and under >= right:
        sys.stdout.write(f"{under}\n{sx} {sy - 1}\n")
    elif above >= under and above >= left and above >= right:
        sys.stdout.write(f"{above}\n{sx} {sy + 1}\n")
    elif left >= under and left >= above and left >= right:
        sys.stdout.write(f"{left}\n{sx - 1} {sy}\n")
    elif right >= under and right >= above and right >= left:
        sys.stdout.write(f"{right}\n{sx + 1} {sy}\n")

if __name__ == "__main__":
    alif()
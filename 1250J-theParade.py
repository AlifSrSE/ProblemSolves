# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1250/problem/J

import sys

def check(h, rows, t):
    if t <= 0:
        return True

    cnt = 0
    avail = 0
    
    for p in range(len(h)):
        if cnt >= rows:
            break
            
        total = avail + h[p]
        cnt += (total // t)
        new_avail = total % t
        avail = min(h[p], new_avail)
        
    return (cnt >= rows)

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        c = list(map(int, sys.stdin.readline().split()))
        sumc = sum(c)
        left = 0
        right = (sumc // k) + 1 
        res = 0

        while left <= right:
            mid = (left + right) // 2
            
            if check(c, k, mid):
                res = mid * k
                left = mid + 1
            else:
                right = mid - 1
        
        sys.stdout.write(f"{res}\n")

if __name__ == "__main__":
    alif()
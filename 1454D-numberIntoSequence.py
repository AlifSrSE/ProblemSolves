#Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1454/problem/D
 
import math
 
def sieve(n):
    p = [1] * (n + 1)
    p[0] = p[1] = 0
    for i in range(2, int(math.sqrt(len(p))) + 1):
        if p[i] == 0:
            continue
        for j in range(0, len(p)):
            if i * i + i * j >= len(p):
                break
            p[i * i + i * j] = 0
    return p
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ps = sieve(int(math.sqrt(n)) + 1)
        ans = [n]
        
        for i in range(len(ps)):
            if ps[i] == 0:
                continue
            tmp = []
            nc = n
            while nc % i == 0:
                nxt = nc // i
                if nxt % i > 0:
                    break
                tmp.append(i)
                nc = nxt
            tmp.append(nc)
            if len(tmp) > len(ans):
                ans = tmp
        
        print(len(ans))
        print(*ans)
 
if __name__ == "__main__":
    main()

#Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1095/problem/C
 
import math
from heapq import heappush, heappop
 
def main():
    n, k = map(int, input().split())
    pq = []
    curr = n
    
    while curr > 0:
        p = math.floor(math.log2(curr))
        curr -= 2 ** p
        heappush(pq, -p) 
    
    ok = k >= len(pq) and k <= n
    
    if ok:
        k -= len(pq)
        while k > 0:
            p = -heappop(pq)  
            heappush(pq, -(p - 1))
            heappush(pq, -(p - 1))
            k -= 1
    
    if ok:
        print("YES")
        result = []
        while pq:
            result.append(2 ** (-heappop(pq)))
        print(" ".join(map(str, result)))
    else:
        print("NO")
 
if __name__ == "__main__":
    main()

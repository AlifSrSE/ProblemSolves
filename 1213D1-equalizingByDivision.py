#Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1213/problem/D1
 
import sys
from collections import defaultdict
 
def min_operations(n, k, a):
    a.sort()
    kit = defaultdict(list)
    
    for num in a:
        kit[num].append(0)
        steps = 0
        while num > 0:
            num //= 2
            steps += 1
            kit[num].append(steps)
    
    ans = float('inf')
    for it in kit.values():
        if len(it) >= k:
            it.sort()
            ans = min(ans, sum(it[:k]))
    
    return ans
 
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:]))
    print(min_operations(n, k, a))
 
if __name__ == "__main__":
    main()

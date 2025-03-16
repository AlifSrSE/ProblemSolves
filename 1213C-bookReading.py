# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1213/problem/C
 
import sys
 
def sum_of_last_digits(n, m):
    if n < m:
        return 0
    
    start = m
    end = (n // m) * m
    cnt = (end - start) // m + 1
    cycle = []
    total_sum = 0
    
    i = 1
    while i * m <= n:
        nxt = (i * m) % 10
        if nxt in cycle:
            break
        cycle.append(nxt)
        total_sum += nxt
        i += 1
    
    ans = total_sum * (cnt // len(cycle))
    rem = cnt % len(cycle)
    
    for i in range(rem):
        ans += cycle[i]
    
    return ans
 
def main():
    input = sys.stdin.read
    data = input().split()
    q = int(data[0])
    index = 1
    results = []
    for _ in range(q):
        n, m = map(int, data[index:index+2])
        index += 2
        results.append(str(sum_of_last_digits(n, m)))
    print("\n".join(results))
 
if __name__ == "__main__":
    main()
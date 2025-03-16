# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/E
 
from sys import stdin
input = stdin.readline
 
def main():
    t = int(input().strip())
    
    for _ in range(t):
        n, s = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        
        if min(a) > s:
            print(-1)
            continue
            
        curr_sum = 0
        left = 0
        max_len = 0
        
        for right in range(n):
            curr_sum += a[right]
            
            while curr_sum > s and left <= right:
                curr_sum -= a[left]
                left += 1
            
            if curr_sum == s:
                max_len = max(max_len, right - left + 1)
            
            if left == right + 1 and n - right - 1 + max_len <= max_len:
                break
        
        total_sum = sum(a[left:]) + (curr_sum if left <= right else 0)
        if total_sum < s or max_len == 0:
            print(-1)
        else:
            print(n - max_len)
 
if __name__ == "__main__":
    main()
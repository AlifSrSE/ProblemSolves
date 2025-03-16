# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/D
 
import sys
import heapq
 
def solve():
    n = int(sys.stdin.readline()) 
    gates = [sys.stdin.readline().split() for _ in range(n)]
 
    dp = {1: 1} 
    MAX_STATES = 1000  
 
    for left_op, left_val, right_op, right_val in gates:
        left_val, right_val = int(left_val), int(right_val)
        new_dp = {}
 
        heap = [(-l - r, l, r) for l, r in dp.items()]
        heapq.heapify(heap)
 
        for _ in range(min(MAX_STATES, len(heap))):
            _, left, right = heapq.heappop(heap)
            left_add = left_val if left_op == '+' else left * (left_val - 1)
            right_add = right_val if right_op == '+' else right * (right_val - 1)
            total = left_add + right_add
 
            new_left0, new_right0 = left, right + total
            new_left1, new_right1 = left + total, right
 
            if new_left0 in new_dp:
                new_dp[new_left0] = max(new_dp[new_left0], new_right0)
            else:
                new_dp[new_left0] = new_right0
 
            if new_left1 in new_dp:
                new_dp[new_left1] = max(new_dp[new_left1], new_right1)
            else:
                new_dp[new_left1] = new_right1
 
        dp = dict(heapq.nlargest(MAX_STATES, new_dp.items(), key=lambda x: x[0] + x[1]))
 
    print(max(left + right for left, right in dp.items()))
 
t = int(sys.stdin.readline())
for _ in range(t):
    solve()
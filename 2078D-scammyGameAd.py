# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/D
 
def solve():
    n = int(input())
    gates = []
    for _ in range(n):
        line = input().strip()
        parts = line.split()
        left_gate = f"{parts[0]} {parts[1]}" 
        right_gate = f"{parts[2]} {parts[3]}"  
        gates.append((left_gate, right_gate))
    
    dp = {(1, 1): 2}
    
    for left_gate, right_gate in gates:
        left_op, left_val = left_gate[0], int(left_gate[2:])
        right_op, right_val = right_gate[0], int(right_gate[2:])
        
        new_dp = {}
        for (left, right), _ in dp.items():
            left_add = left_val if left_op == '+' else left * (left_val - 1)
            right_add = right_val if right_op == '+' else right * (right_val - 1)
            total_new = left_add + right_add
            
            for i in range(total_new + 1):
                new_left = left + i
                new_right = right + (total_new - i)
                new_total = new_left + new_right
                new_dp[(new_left, new_right)] = max(new_dp.get((new_left, new_right), 0), new_total)
        
        dp = new_dp
    
    print(max(dp.values()))
 
t = int(input())
for _ in range(t):
    solve()

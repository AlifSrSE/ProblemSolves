# Author: AlifSrSE
import sys
from bisect import bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    output = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        q = int(input_data[ptr + 1])
        ptr += 2
        
        a = sorted([int(x) for x in input_data[ptr : ptr + n]])
        ptr += n
        
        queries = [int(x) for x in input_data[ptr : ptr + q]]
        ptr += q
        
        # Precompute prefix sums for O(1) range sum calculation
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
            
        possible_sums = set()
        
        def search(l, r):
            # Calculate range sum using prefix sums
            current_sum = pref[r+1] - pref[l]
            possible_sums.add(current_sum)
            
            # Base case: if all elements in range are the same
            if a[l] == a[r]:
                return
            
            mid_val = (a[l] + a[r]) // 2
            # Use binary search to find the split point efficiently
            mid_idx = bisect_right(a, mid_val, l, r + 1) - 1
            
            search(l, mid_idx)
            search(mid_idx + 1, r)
            
        search(0, n - 1)
        
        case_res = ["Yes" if s in possible_sums else "No" for s in queries]
        output.append("\n".join(case_res))
        
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    
    solve()
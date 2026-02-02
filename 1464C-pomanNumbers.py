# Author: AlifSrSE
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t_idx = 0
    t = int(input_data[t_idx])
    t_idx += 1
    results = []
    
    for _ in range(t):
        n = int(input_data[t_idx])
        m = int(input_data[t_idx + 1])
        t_idx += 2
        
        a = [int(x) for x in input_data[t_idx : t_idx + n]]
        t_idx += n
        
        # Find the last index where the array is NOT sorted
        # In Java: minLength is the length of the prefix that needs to be sorted
        min_length = n
        while min_length > 0 and a[min_length - 1] == min_length:
            min_length -= 1
        
        # Combined probability of failure (not being sorted)
        # Prob(Sorted) = 1 - Prob(Never sorted)
        # Prob(Never sorted) = Product of (1 - p_i) for all valid operations
        prob_fail = 1.0
        found_valid_op = False
        
        for _ in range(m):
            r = int(input_data[t_idx])
            p = float(input_data[t_idx + 1])
            t_idx += 2
            
            if r >= min_length:
                found_valid_op = True
                prob_fail *= (1.0 - p)
        
        if min_length == 0:
            results.append(f"{1.0:.9f}")
        elif not found_valid_op:
            results.append(f"{0.0:.9f}")
        else:
            results.append(f"{1.0 - prob_fail:.9f}")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
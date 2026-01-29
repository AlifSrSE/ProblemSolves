# Author: AlifSrSE
import sys

def compute_gap(a, index, target_index):
    n = len(a)
    if target_index == -1 or target_index == n:
        return float('inf')

    val = a[target_index]
    before = val if index == 0 else a[index - 1]
    after = val if index == n - 1 else a[index + 1]

    return abs(before - val) + abs(after - val)

def solve(a):
    n = len(a)
    if n < 2: return 0
    
    base_sum = sum(abs(a[i] - a[i+1]) for i in range(n - 1))
    
    min_delta = 0
    for i in range(n):
        before_val = 0 if i == 0 else abs(a[i] - a[i-1])
        after_val = 0 if i == n-1 else abs(a[i] - a[i+1])
        current_local_gap = before_val + after_val
        best_new_local = min(compute_gap(a, i, i - 1), compute_gap(a, i, i + 1))
        
        delta = best_new_local - current_local_gap
        if delta < min_delta:
            min_delta = delta
            
    return base_sum + min_delta

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        a = [int(x) for x in input_data[ptr + 1 : ptr + 1 + n]]
        results.append(str(solve(a)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2057/problem/B

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    counts = {}
    unique_vals = set()
    for val in a:
        counts[val] = counts.get(val, 0) + 1
        unique_vals.add(val)
        
    sorted_counts = sorted((count, val) for val, count in counts.items())
    
    remaining_unique = len(unique_vals)
    total_removed = 0
    
    for count, val in sorted_counts:
        if total_removed + count <= k:
            remaining_unique -= 1
            total_removed += count
        else:
            break
            
    print(max(1, remaining_unique))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
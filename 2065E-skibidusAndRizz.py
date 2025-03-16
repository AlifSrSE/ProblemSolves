# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2065/problem/E

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, m, k = map(int, data[i].split())
        
        if k > n + m:
            results.append("-1")
            continue
        
        if k > max(n, m):
            results.append("-1")
            continue
        
        if n >= m:
            zeros = min(k, n)
            ones = k - zeros
            if ones > m:
                results.append("-1")
                continue
            s = "0" * zeros + "1" * ones
            remaining_zeros = n - zeros
            remaining_ones = m - ones
            s += "0" * remaining_zeros + "1" * remaining_ones
        else:
            ones = min(k, m)
            zeros = k - ones
            if zeros > n:
                results.append("-1")
                continue
            s = "1" * ones + "0" * zeros
            remaining_ones = m - ones
            remaining_zeros = n - zeros
            s += "1" * remaining_ones + "0" * remaining_zeros
        
        results.append(s)
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
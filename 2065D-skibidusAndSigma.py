# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/D
 
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, (data[index], data[index + 1]))
        index += 2
        v = []
        total = 0
        
        for _ in range(n):
            row = list(map(int, data[index:index + m]))
            index += m
            sum_row = sum(row)
            v.append(sum_row)
            
            for q in range(m):
                total += (m - q) * row[q]
        
        v.sort(reverse=True)
        for p in range(n):
            total += (n - 1 - p) * m * v[p]
        
        results.append(str(total))
    
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    solve()
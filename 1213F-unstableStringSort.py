# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1213/problem/E
 
import sys
 
def restore_string(n, k, p, q):
    s = [None] * n
    rank = [0] * n
    
    for i in range(n):
        rank[p[i] - 1] = i
        rank[q[i] - 1] = max(rank[q[i] - 1], i)
    
    distinct_count = 0
    char_map = {}
    result = [''] * n
    
    for i in sorted(range(n), key=lambda x: rank[x]):
        if i == 0 or rank[i] != rank[i - 1]:
            distinct_count += 1
        char_map[i] = chr(97 + min(distinct_count - 1, k - 1))
    
    for i in range(n):
        result[p[i] - 1] = char_map[i]
    
    return "YES\n" + "".join(result)
 
def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, k = data[0], data[1]
    p = data[2:n+2]
    q = data[n+2:2*n+2]
    print(restore_string(n, k, p, q))
 
if __name__ == "__main__":
    main()

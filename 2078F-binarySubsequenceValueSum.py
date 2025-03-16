# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/F
 
def solve():
    n, q = map(int, input().split())
    s = list(input())
    mod = 998244353
 
    def calculate_f(v, l, r):
        if l > r:
            return 0
        zeros = 0
        for i in range(l, r + 1):
            if v[i] == '0':
                zeros += 1
        return r - l + 1 - 2 * zeros
 
    def calculate_score(v):
        if not v:
            return 0
        max_score = 0
        length = len(v)
        for i in range(length + 1):
            max_score = max(max_score, calculate_f(v, 0, i - 1) * calculate_f(v, i, length - 1))
        return max_score
 
    def calculate_subsequence_sum(current_s):
        total_score = 0
        for mask in range(1, 1 << len(current_s)):
            subsequence = []
            for i in range(len(current_s)):
                if (mask >> i) & 1:
                    subsequence.append(current_s[i])
            total_score = (total_score + calculate_score(subsequence)) % mod
        return total_score
 
    for _ in range(q):
        i = int(input()) - 1
        s[i] = '1' if s[i] == '0' else '0'
        print(calculate_subsequence_sum(s))
 
t = int(input())
for _ in range(t):
    solve()
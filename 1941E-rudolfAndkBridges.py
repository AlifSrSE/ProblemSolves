# Author : AlifSrSE
# Date : 2025-03-11
# Problem link : https://codeforces.com/contest/1941/problem/E

import sys

input = sys.stdin.readline
INF = 0x3f3f3f3f3f3f3f3f

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [INF] * (4 * n)
    
    def update(self, k, l, r, x, v):
        if l == r and l == x:
            self.tree[k] = v
            return
        if x < l or x > r:
            return
        mid = (l + r) // 2
        self.update(2 * k, l, mid, x, v)
        self.update(2 * k + 1, mid + 1, r, x, v)
        self.tree[k] = min(self.tree[2 * k], self.tree[2 * k + 1])
    
    def query(self, k, l, r, x, y):
        if y < l or x > r:
            return INF
        if x <= l and r <= y:
            return self.tree[k]
        mid = (l + r) // 2
        return min(self.query(2 * k, l, mid, x, y),
                  self.query(2 * k + 1, mid + 1, r, x, y))

def main():
    T = int(input())
    for _ in range(T):
        n, m, num, d = map(int, input().split())
        ans = [0] * (n + 1)
        f = [0] * (m + 1)  
        seg = SegmentTree(m)
        
        for i in range(1, n + 1):
            a = [0] + list(map(int, input().split()))
            f[1] = 1
            seg.tree = [INF] * (4 * m)
            seg.update(1, 1, m, 1, 1)
            
            for j in range(2, m + 1):
                f[j] = seg.query(1, 1, m, max(j - d - 1, 1), max(j - 1, 1)) + a[j] + 1
                seg.update(1, 1, m, j, f[j])
            
            ans[i] = f[m]
        
        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        
        min_sum = INF
        for i in range(1, n - num + 2):
            min_sum = min(min_sum, ans[i + num - 1] - ans[i - 1])
        
        print(min_sum)

if __name__ == "__main__":
    main()
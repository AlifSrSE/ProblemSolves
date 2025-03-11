# Author : AlifSrSE
# Date : 2025-03-11
# Problem link : https://codeforces.com/contest/1843/problem/E

def check(n, l, r, x, change_num):
    a = [0] * n
    for i in range(change_num):
        a[x[i] - 1] = 1
    
    prefix_sums = [0] * n
    prefix_sums[0] = a[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + a[i]
    
    for i in range(len(l)):
        ones = prefix_sums[r[i]-1] - (0 if l[i] == 1 else prefix_sums[l[i]-2])
        length = r[i] - l[i] + 1
        zeros = length - ones
        if ones > zeros:
            return True
    return False

def solve(n, l, r, x):
    if not check(n, l, r, x, len(x)):
        return -1
        
    left = 0
    right = len(x)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if check(n, l, r, x, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    
    q = int(input())
    x = []
    for _ in range(q):
        x.append(int(input()))
    
    print(solve(n, l, r, x))
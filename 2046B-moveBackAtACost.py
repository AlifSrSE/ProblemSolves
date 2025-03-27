# Author : AlifSrSE
# Date : 2025-03-27
# Problem link : https://codeforces.com/contest/2046/problem/B

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    result = a[:]
    visited = {tuple(a)}
    q = [(a[:], 0)]

    while q:
        curr_a, ops = q.pop(0)

        if curr_a < result:
            result = curr_a[:]

        if ops < 2 * n: 
            for i in range(len(curr_a)):
                new_a = curr_a[:]
                new_a[i] += 1
                new_a = new_a[:i] + new_a[i+1:] + [new_a[i]]
                new_tuple = tuple(new_a)
                if new_tuple not in visited:
                    visited.add(new_tuple)
                    q.append((new_a, ops + 1))

    print(*result)

t = int(input())
for _ in range(t):
    solve()
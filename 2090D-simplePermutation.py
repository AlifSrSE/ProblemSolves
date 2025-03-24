# Author: AlifSrSe
# date: 2025-03-23
# https://codeforces.com/problemset/problem/2090/D
 
import sys
 
input = sys.stdin.read
data = input().split()
index = 0
 
def get_int():
    global index
    val = int(data[index])
    index += 1
    return val
 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def solve(n):
    perm = [2, 1] + list(range(3, n + 1))
    c = []
    s = 0
    for i in range(n):
        s += perm[i]
        c.append((s + i) // (i + 1))
    primes = sum(1 for x in c if is_prime(x))
    target = (n // 3) - 1
    if n > 2 and primes < target:
        perm = list(range(n, 0, -1))
    return perm
 
t = get_int()
for _ in range(t):
    n = get_int()
    result = solve(n)
    print(" ".join(map(str, result)))
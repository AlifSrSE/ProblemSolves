# Author: AlifSrSe
# date: 2025-03-23
# https://codeforces.com/problemset/problem/2090/E1
 
import sys
 
input = sys.stdin.read
data = input().split()
index = 0
 
def get_int():
    global index
    val = int(data[index])
    index += 1
    return val
 
def get_array(n):
    global index
    arr = [int(data[index + i]) for i in range(n)]
    index += n
    return arr
 
def solve():
    n, k = get_int(), get_int()
    a = get_array(n)
    b = get_array(n)
    if sum(a) == 0:
        return 0
    rounds = 0
    while max(a) > 0:
        rounds += 1
        t = [min(a[i], b[i]) for i in range(n)]
        a = [a[i] - t[i] for i in range(n)]
        b = [b[i] - t[i] for i in range(n)]
        a = a[-1:] + a[:-1]
        if rounds > n and max(a) > 0:
            return rounds
    return rounds
 
t = get_int()
for _ in range(t):
    print(solve())

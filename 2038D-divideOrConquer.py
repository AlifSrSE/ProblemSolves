# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import defaultdict

N = 200100
M = 7000010
MOD = 998244353

n = 0
a = [0] * N
f = [0] * N
stuff = [None] * M 

def update(p, v):
    p += 1
    while p < N:
        f[p] = (f[p] + v) % MOD
        p += p & (-p)

def prefix(p):
    p += 1
    res = 0
    while p:
        res = (res + f[p]) % MOD
        p -= p & (-p)
    return res

def query(l, r):
    res = (prefix(r) - prefix(l - 1)) % MOD
    return res

def main():
    global n
    n = int(input())
    a[1:n+1] = list(map(int, input().split()))
    
    vec = []
    top = 0
    
    for i in range(1, n + 1):
        vec.append((i, a[i]))
        new_vec = []
        
        for j, value in vec:
            value |= a[i]
            if not new_vec or new_vec[-1][1] != value:
                new_vec.append((j, value))
        
        vec = new_vec
        
        for j in range(len(vec)):
            end_pos = vec[j + 1][0] - 1 if j + 1 < len(vec) else i
            stuff[top] = [vec[j][1], i, vec[j][0], end_pos]
            top += 1
    
    stuff_array = sorted(stuff[:top], key=lambda x: x[0])
    
    update(0, 1)
    i = 0
    while i < top:
        j = i
        while j < top and stuff_array[j][0] == stuff_array[i][0]:
            update(stuff_array[j][1], query(stuff_array[j][2] - 1, stuff_array[j][3] - 1))
            j += 1
        i = j
    
    print(query(n, n))

if __name__ == "__main__":
    main()
# Author: AlifSrSe
# date: 2025-03-23
# https://codeforces.com/problemset/problem/2090/E1
 
import sys
from collections import deque

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
    arr = list(map(int, data[index:index + n]))
    index += n
    return arr

def solve():
    n, k = get_int(), get_int()
    a = deque(get_array(n))  
    b = get_array(n)

    if all(v == 0 for v in a):  
        return 0  

    rounds = 0
    seen_states = set()
    
    while True:
        rounds += 1
        has_positive = False 

        for i in range(n):
            reduction = min(a[i], b[i])
            a[i] -= reduction
            b[i] -= reduction
            if a[i] > 0:
                has_positive = True

        if not has_positive:
            return rounds  

        a.rotate(1) 

        state_hash = hash(tuple(a))
        if state_hash in seen_states:
            return -1  
        seen_states.add(state_hash)

        if rounds > n:
            return rounds  

t = get_int()
results = [str(solve()) for _ in range(t)]
sys.stdout.write("\n".join(results) + "\n")  

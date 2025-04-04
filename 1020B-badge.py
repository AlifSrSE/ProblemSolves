# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def find_two_hole(p, begin_index):
    visited = [False] * len(p)
    
    i = begin_index
    while True:
        if visited[i]:
            return i + 1
        visited[i] = True
        i = p[i] - 1

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    result = [find_two_hole(p, i) for i in range(n)]
    return result

print(' '.join(map(str, solve())))
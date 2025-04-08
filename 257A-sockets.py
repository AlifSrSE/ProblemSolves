# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve_sockets():
    n, m, k = map(int, input().split())
    sockets = list(map(int, input().split()))
    
    sockets.sort()
    
    output = 0
    
    if m > k:
        m -= k
        for u in range(n-1, -1, -1):
            m -= (sockets[u] - 1)
            if m <= 0:
                break
        if m <= 0:
            output = n - u
        else:
            output = -1
    
    print(output)
solve_sockets()
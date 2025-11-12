# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    data_idx = 1

    if n == 0:
        sys.stdout.write("0\n\n")
        return
    a = [int(data[data_idx + i]) for i in range(n)]
    
    if n <= 1:
        sys.stdout.write(f"0\n{a[0]}\n")
        return

    a.sort(reverse=True)
    b = [0] * n

    for p in range(1, n, 2):
        b[p] = a.pop()
        
    for p in range(n):
        if b[p] == 0:
            b[p] = a.pop()
            
    cnt = 0
    for p in range(1, n - 1):
        if b[p - 1] > b[p] and b[p] < b[p + 1]:
            cnt += 1
            
    sys.stdout.write(f"{cnt}\n")
    sys.stdout.write(" ".join(map(str, b)) + "\n")
alif()
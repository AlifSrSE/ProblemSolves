# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    pointer = 1
    output = []

    for _ in range(t):
        n = int(data[pointer])
        m = int(data[pointer + 1])
        pointer += 2
        
        a = []
        for i in range(n):
            a.append(data[pointer + i])
        pointer += n
        cnt = 0

        for p in range(n):
            if a[p][m - 1] == 'R':
                cnt += 1
        
        for p in range(m):
            if a[n - 1][p] == 'D':
                cnt += 1
        output.append(str(cnt))
    sys.stdout.write('\n'.join(output) + '\n')

alif()
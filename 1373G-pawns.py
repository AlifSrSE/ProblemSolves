# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

input = sys.stdin.readline
n,k,m = map(int,input().split())
pawns = set()
max_need = 0
count = [0]*(2*n+2)

def need(x,y):
    return y + abs(x - k)
for _ in range(m):
    x,y = map(int,input().split())
    if (x,y) in pawns:
        pawns.remove((x,y))
        count[need(x,y)] -= 1
    else:
        pawns.add((x,y))
        count[need(x,y)] += 1
    while max_need < 2*n+1 and count[max_need+1] > 0:
        max_need += 1
    while max_need > 0 and count[max_need] == 0:
        max_need -= 1
    print(max(0, max_need - n))
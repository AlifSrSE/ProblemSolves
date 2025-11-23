# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
pos=[]
for i,x in enumerate(a):
    if x==1: pos.append(i+1)
m=len(pos)
maxC=n*(n-1)//2

NEG=-10**18

dp=[ [ [NEG]*(n+1) for _ in range(maxC+1) ] for _ in range(m+1) ]
dp[0][0][0]=0

from math import comb

for i in range(1,n+1):
    ndp=[ [ [NEG]*(n+1) for _ in range(maxC+1) ] for _ in range(m+1) ]
    for used in range(m+1):
        pu=pos[used] if used<m else None
        for c in range(maxC+1):
            for r in range(n+1):
                v=dp[used][c][r]
                if v<0: continue
                nr=r+1
                if nr<=n and ndp[used][c][nr]<v:
                    ndp[used][c][nr]=v
                if used<m:
                    cost=abs(i-pu)
                    nc=c+cost
                    if nc<=maxC:
                        nv=v+(r*(r-1))//2
                        if ndp[used+1][nc][0]<nv:
                            ndp[used+1][nc][0]=nv
    dp=ndp

T=n-m
tot=T*(T-1)//2
res=[0]*(maxC+1)

for c in range(maxC+1):
    best=NEG
    for r in range(n+1):
        v=dp[m][c][r]
        if v>=0:
            val=v+(r*(r-1))//2
            if val>best: best=val
    if c>0 and res[c-1]>best:
        best=res[c-1]
    res[c]=tot-best

print(*res)

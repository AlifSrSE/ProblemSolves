# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
input=sys.stdin.readline
mod=998244353
n,k=map(int,input().split())
events=[]

for _ in range(n):
    l,r=map(int,input().split())
    events.append((l,1))
    events.append((r+1,-1))

events.sort()
mx=n
fact=[1]*(mx+1)
inv=[1]*(mx+1)

for i in range(1,mx+1):
    fact[i]=fact[i-1]*i%mod
inv[mx]=pow(fact[mx],mod-2,mod)

for i in range(mx,0,-1):
    inv[i-1]=inv[i]*i%mod

def C(a,b):
    if b<0 or b>a: return 0
    return fact[a]*inv[b]%mod*inv[a-b]%mod

ans=0
cur=0
i=0
m=len(events)

while i<m:
    t=events[i][0]
    add=0
    rem=0
    while i<m and events[i][0]==t:
        if events[i][1]==1: add+=1
        else: rem+=1
        i+=1
    if add:
        ans = (ans + C(cur, k-1)*add)%mod
    cur += add
    cur -= rem

print(ans)

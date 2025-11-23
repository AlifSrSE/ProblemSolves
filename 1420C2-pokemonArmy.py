# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
input=sys.stdin.readline

class Node:
    __slots__=("x00","x01","x10","x11")
    def __init__(self,a=None):
        if a is None:
            self.x00=self.x01=self.x10=self.x11=-(10**30)
        else:
            self.x00=0
            self.x01=-(10**30)
            self.x10=-(10**30)
            self.x11=a

def merge(L,R,res):
    res.x00 = max(L.x00+R.x00, L.x01+R.x10)
    res.x01 = max(L.x00+R.x01, L.x01+R.x11)
    res.x10 = max(L.x10+R.x00, L.x11+R.x10)
    res.x11 = max(L.x10+R.x01, L.x11+R.x11)

class Seg:
    def __init__(self,a,n):
        self.n=n
        self.t=[Node() for _ in range(4*n)]
        self.a=a
        self.build(1,1,n)

    def build(self,v,l,r):
        if l==r:
            self.t[v]=Node(self.a[l])
            return
        m=(l+r)//2
        self.build(v*2,l,m)
        self.build(v*2+1,m+1,r)
        cur=Node()
        merge(self.t[v*2],self.t[v*2+1],cur)
        self.t[v]=cur

    def update(self,v,l,r,pos,val):
        if l==r:
            self.t[v]=Node(val)
            return
        m=(l+r)//2
        if pos<=m:
            self.update(v*2,l,m,pos,val)
        else:
            self.update(v*2+1,m+1,r,pos,val)
        cur=Node()
        merge(self.t[v*2],self.t[v*2+1],cur)
        self.t[v]=cur

t=int(input())
out=[]

for _ in range(t):
    n,q=map(int,input().split())
    arr=[0]+list(map(int,input().split()))
    seg=Seg(arr,n)
    out.append(str(seg.t[1].x11))

    for __ in range(q):
        l,r=map(int,input().split())
        if l!=r:
            arr[l],arr[r]=arr[r],arr[l]
            seg.update(1,1,n,l,arr[l])
            seg.update(1,1,n,r,arr[r])
        out.append(str(seg.t[1].x11))

print("\n".join(out))

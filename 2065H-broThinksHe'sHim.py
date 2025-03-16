# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/H
 
import sys
 
MOD = 998244353
 
def power(a, b, mod=MOD):
    return pow(a, b, mod)
 
def mul(a, b, mod=MOD):
    return (a * b) % mod
 
class Fenwick:
    def __init__(self, n):
        self.n = n + 1
        self.tree = [0] * self.n
    
    def add(self, i, d):
        while i < self.n:
            self.tree[i] = (self.tree[i] + d) % MOD
            i += i & -i
    
    def ask(self, i):
        sum = 0
        while i > 0:
            sum = (sum + self.tree[i]) % MOD
            i -= i & -i
        return sum
    
    def range_sum(self, l, r):
        return (self.ask(r) - self.ask(l - 1)) % MOD
 
class MInt:
    Mod = MOD
    
    def __init__(self, x=0):
        self.x = x % MInt.Mod
    
    def __neg__(self):
        return MInt(MInt.Mod - self.x if self.x != 0 else 0)
    
    def __add__(self, other):
        return MInt(self.x + other.x)
    
    def __sub__(self, other):
        return MInt(self.x - other.x)
    
    def __mul__(self, other):
        return MInt(self.x * other.x % MInt.Mod)
    
    def __truediv__(self, other):
        return self * other.inv()
    
    def inv(self):
        return MInt(power(self.x, MInt.Mod - 2))
    
    def __repr__(self):
        return str(self.x)
 
def enjoyerist():
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    T = int(data[idx]) 
    idx += 1
    result = []
    
    for _ in range(T):
        s = data[idx].strip()
        n = len(s)
        s = "#" + s
        idx += 1
        
        power2 = [1] * (n + 1)
        for i in range(1, n + 1):
            power2[i] = power2[i - 1] * 2 % MOD
        
        pre = [Fenwick(n) for _ in range(2)]
        suf = [Fenwick(n) for _ in range(2)]
        
        for i in range(1, n + 1):
            t = int(s[i] == '1')
            pre[t].add(i, power2[i - 1])
            suf[t].add(i, power2[n - i])
        
        ans = power2[n] - 1
        for i in range(1, n + 1):
            t = int(s[i] == '1')
            ans = (ans + power2[i - 1] * suf[1 - t].range_sum(i + 1, n)) % MOD
        
        q = int(data[idx])
        idx += 1
        
        queries = list(map(int, data[idx].split()))
        idx += 1
        
        res = []
        for x in queries:
            t = int(s[x] == '1')
            
            if x + 1 <= n:
                ans = (ans - power2[x - 1] * suf[1 - t].range_sum(x + 1, n)) % MOD
                ans = (ans + power2[x - 1] * suf[t].range_sum(x + 1, n)) % MOD
            
            if x - 1 >= 1:
                ans = (ans - power2[n - x] * pre[1 - t].range_sum(1, x - 1)) % MOD
                ans = (ans + power2[n - x] * pre[t].range_sum(1, x - 1)) % MOD
            
            pre[t].add(x, -power2[x - 1])
            suf[t].add(x, -power2[n - x])
            
            s = s[:x] + ('0' if t == 1 else '1') + s[x + 1:]
            t = 1 - t
            
            pre[t].add(x, power2[x - 1])
            suf[t].add(x, power2[n - x])
            
            res.append(str(ans))
        
        result.append(" ".join(res))
  
    sys.stdout.write("\n".join(result) + "\n")
enjoyerist()

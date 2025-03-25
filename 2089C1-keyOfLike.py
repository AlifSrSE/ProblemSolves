# Author: AlifSrSe
# date: 2025-03-25
# https://codeforces.com/problemset/problem/2089/C1
 
class ModIntBase:
    P = 1000000007

    def __init__(self, x=0):
        if isinstance(x, int):
            self.x = x % ModIntBase.P
        else:
            self.x = x.x

    @staticmethod
    def mod():
        return ModIntBase.P

    def val(self):
        return self.x

    def __neg__(self):
        res = ModIntBase()
        res.x = 0 if self.x == 0 else ModIntBase.mod() - self.x
        return res

    def inv(self):
        return self.power(ModIntBase.mod() - 2)

    def __mul__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        return ModIntBase(self.val() * rhs.val() % ModIntBase.mod())

    def __imul__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        self.x = self.val() * rhs.val() % ModIntBase.mod()
        return self

    def __add__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        res = ModIntBase(self.val() + rhs.val())
        if res.val() >= ModIntBase.mod():
            res.x -= ModIntBase.mod()
        return res

    def __iadd__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        self.x += rhs.val()
        if self.x >= ModIntBase.mod():
            self.x -= ModIntBase.mod()
        return self

    def __sub__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        res = ModIntBase(self.val() - rhs.val())
        if res.val() >= ModIntBase.mod():
            res.x += ModIntBase.mod()
        return res

    def __isub__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        self.x -= rhs.val()
        if self.x >= ModIntBase.mod():
            self.x += ModIntBase.mod()
        return self

    def __truediv__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        return self * rhs.inv()

    def __itruediv__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        self *= rhs.inv()
        return self

    def __str__(self):
        return str(self.val())

    def __repr__(self):
        return str(self.val())

    def __eq__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        return self.val() == rhs.val()

    def __lt__(self, rhs):
        if isinstance(rhs, int):
          rhs = ModIntBase(rhs)
        return self.val() < rhs.val()

    def power(self, b):
        a = ModIntBase(self)
        res = ModIntBase(1)
        while b != 0:
            if b & 1:
                res *= a
            a *= a
            b //= 2
        return res

class Comb:
    def __init__(self, n=0):
        self.n = 0
        self._fac = [ModIntBase(1)]
        self._invfac = [ModIntBase(1)]
        self._inv = [ModIntBase(0)]
        if n > 0:
            self.init(n)

    def init(self, m):
        if m <= self.n:
            return
        self._fac.extend([ModIntBase()] * (m - self.n))
        self._invfac.extend([ModIntBase()] * (m - self.n))
        self._inv.extend([ModIntBase()] * (m - self.n))

        for i in range(self.n + 1, m + 1):
            self._fac[i] = self._fac[i - 1] * i
        self._invfac[m] = self._fac[m].inv()
        for i in range(m, self.n, -1):
            self._invfac[i - 1] = self._invfac[i] * i
            self._inv[i] = self._invfac[i] * self._fac[i - 1]
        self.n = m

    def fac(self, m):
        if m > self.n:
            self.init(2 * m)
        return self._fac[m]

    def invfac(self, m):
        if m > self.n:
            self.init(2 * m)
        return self._invfac[m]

    def inv(self, m):
        if m > self.n:
            self.init(2 * m)
        return self._inv[m]

    def binom(self, n, m):
        if n < m or m < 0:
            return ModIntBase(0)
        return self.fac(n) * self.invfac(m) * self.invfac(n - m)

def solve():
    n, l, k = map(int, input().split())
    
    comb = Comb(2 * n)
    
    dp = [ModIntBase(0) for _ in range(n)]
    dp[0] = ModIntBase(1)
    
    ans = [ModIntBase(0) for _ in range(n)]
    
    for x in range(l, 0, -1):
        ndp = [ModIntBase(0) for _ in range(n)]
        f = [ModIntBase(0) for _ in range(n)]
        for i in range(1, x + 1):
            f[i % n] += comb.inv(x)
        for i in range(n):
            for j in range(n):
                ndp[(i + j) % n] += dp[i] * f[j]
        dp = ndp[:]
        for i in range(n):
            ans[i] += dp[(i + 1) % n]
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
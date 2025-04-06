# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
N = 1 << 21

class Mint:
    def __init__(self, x=0):
        self.x = x % MOD

    def __iadd__(self, other):
        self.x = (self.x + other.x) % MOD
        return self

    def __isub__(self, other):
        self.x = (self.x - other.x + MOD) % MOD
        return self

    def __imul__(self, other):
        self.x = (self.x * other.x) % MOD
        return self

    def __itruediv__(self, other):
        return self.__imul__(other ** (MOD - 2))

    def __add__(self, other):
        return Mint(self.x).__iadd__(other)

    def __sub__(self, other):
        return Mint(self.x).__isub__(other)

    def __mul__(self, other):
        return Mint(self.x).__imul__(other)

    def __truediv__(self, other):
        return Mint(self.x).__itruediv__(other)

    def __pow__(self, power):
        result = Mint(1)
        base = Mint(self.x)
        while power:
            if power & 1:
                result *= base
            base *= base
            power >>= 1
        return result

    def __repr__(self):
        return str(self.x)

# Globals
a = [0] * N
ma = [0] * N
dp = [Mint() for _ in range(N)]

class StackSum:
    def __init__(self):
        self.stk = [0] * N
        self.top = 0
        self.sum = Mint(0)

    def reset(self):
        self.top = 0
        self.sum = Mint(0)

    def inc(self, i):
        while self.top and ma[i] >= ma[self.stk[self.top]]:
            self.top -= 1
            if self.top:
                delta = ma[self.stk[self.top]] - ma[self.stk[self.top + 1]]
                self.sum -= Mint(delta) * dp[self.stk[self.top]]
        self.stk[self.top + 1] = i
        if self.top:
            delta = ma[self.stk[self.top]] - ma[self.stk[self.top + 1]]
            self.sum += Mint(delta) * dp[self.stk[self.top]]
        self.top += 1
        return self.sum

ds = [StackSum(), StackSum()]

def main_case():
    length = int(input())
    s = input().strip()[::-1]  
    if all(c == s[0] for c in s):
        print(len(s) - 1)
        return

    n = 0
    len_block = 0
    a_list = []
    for i in range(len(s)):
        len_block += 1
        if i == len(s) - 1 or s[i] != s[i + 1]:
            a[n + 1] = len_block
            n += 1
            len_block = 0

    for i in range(n + 1):
        dp[i] = Mint(0)

    for i in range(1, n):
        if (n - i) % 2 == 0:
            dp[i] = Mint((n - i) // 2)
        else:
            dp[i] = Mint(a[n] + (n - i) // 2)

    for i in range(1, n + 1):
        ma[i] = a[i] + i // 2

    ds[0].reset()
    ds[1].reset()

    for i in range(n, 1, -1):
        dp[i - 1] += Mint(a[i]) * dp[i]
        dp[i - 1] += ds[i & 1].inc(i)

    print((dp[1] * Mint(a[1])).x)

def main():
    t = int(input())
    for _ in range(t):
        main_case()

if __name__ == "__main__":
    main()

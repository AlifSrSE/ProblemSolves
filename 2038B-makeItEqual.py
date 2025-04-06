# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

MOD = 998244353

def power(a, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * a % MOD
        a = a * a % MOD
        n //= 2
    return res

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __repr__(self):
        return str(self.x)

    def __add__(self, other):
        return ModInt(self.x + other.x)

    def __sub__(self, other):
        return ModInt(self.x - other.x)

    def __mul__(self, other):
        return ModInt(self.x * other.x % MOD)

    def __truediv__(self, other):
        return self * other.inv()

    def inv(self):
        return ModInt(power(self.x, MOD - 2))

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    def work(v):
        k = [ModInt(0)] * n
        b = [ModInt(0)] * n
        k[0] = ModInt(1)
        
        for i in range(1, n + 1):
            k[i % n] = ModInt(2) * k[i - 1]
            b[i % n] = ModInt(2) * b[i - 1] - ModInt(a[i - 1]) - ModInt(v)

        x = [0] * n
        x[0] = (b[0] / (ModInt(1) - k[0])).x
        for i in range(1, n):
            x[i] = (k[i] * ModInt(x[0]) + b[i]).x

        mn = min(x)
        x = [xi - mn for xi in x]
        
        p = [0] * n
        for i in range(n):
            p[i] = a[i] - 2 * x[i] + x[(i + 1) % n]
        
        for i in range(n):
            if p[i] < 0 or p[i] != p[(i + 1) % n]:
                return -1

        return sum(x)

    ans = work(0)
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

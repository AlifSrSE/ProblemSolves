# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

class Modular:
    def __init__(self, value=0, mod=10**9 + 7):
        self.mod = mod
        self.value = value % mod
        if self.value < 0:
            self.value += mod

    def __add__(self, other):
        return Modular(self.value + other.value, self.mod)

    def __sub__(self, other):
        return Modular(self.value - other.value, self.mod)

    def __mul__(self, other):
        if isinstance(other, Modular):
            return Modular(self.value * other.value, self.mod)
        else:
            return Modular(self.value * other, self.mod)

    def __truediv__(self, other):
        return self * Modular(pow(other.value, self.mod - 2, self.mod), self.mod)

    def __repr__(self):
        return str(self.value)

def factorial(n, mod):
    fact = [Modular(1, mod)]
    for i in range(1, n + 1):
        fact.append(fact[-1] * Modular(i, mod))
    return fact

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    tt = int(data[index])
    index += 1
    results = []
    
    for _ in range(tt):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        pos = [-1] * n
        for i in range(n):
            if a[i] >= 0:
                pos[a[i]] = i
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if a[i] == -1 else 0)
        
        cnt = [0] * (n + 1)
        for i in range(n):
            for j in range(i + 1, n + 1):
                cnt[pref[j] - pref[i]] += 1
        
        fact = factorial(n, 10**9 + 7)
        coeff = [Modular(1, 10**9 + 7) for _ in range(n + 1)]
        
        L = -1
        R = -1
        skips = 0
        ans = Modular(0, 10**9 + 7)
        
        for val in range(n):
            if pos[val] != -1:
                if L == -1:
                    L = pos[val]
                    R = pos[val] + 1
                    cnt = [0] * (n + 1)
                    for i in range(L + 1):
                        for j in range(R, n + 1):
                            cnt[pref[j] - pref[i]] += 1
                else:
                    while L > pos[val]:
                        for j in range(R, n + 1):
                            cnt[pref[j] - pref[L]] -= 1
                        L -= 1
                    while R <= pos[val]:
                        for i in range(L + 1):
                            cnt[pref[R] - pref[i]] -= 1
                        R += 1
            else:
                for k in range(n + 1):
                    coeff[k] *= Modular(k - skips, 10**9 + 7)
                skips += 1
            
            for k in range(n + 1):
                ans += coeff[k] * Modular(cnt[k], 10**9 + 7) * fact[pref[n] - skips]
        
        results.append(str(ans))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
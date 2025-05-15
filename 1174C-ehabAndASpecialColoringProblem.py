# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1174/problem/C

def build_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def alif(n):
    primes = build_primes(n)
    a = [-1] * (n + 1)
    value = 1
    for prime in primes:
        for i in range(prime, n + 1, prime):
            if a[i] == -1:
                a[i] = value
        value += 1
    return a[2:]

if __name__ == "__main__":
    n = int(input())
    print(" ".join(map(str, alif(n))))

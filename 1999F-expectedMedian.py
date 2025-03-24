# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/F
 
MODULUS = 1_000_000_007
LIMIT = 200000

factorials = [0] * (LIMIT + 1)
factorial_invs = [0] * (LIMIT + 1)

def precompute():
    global factorials, factorial_invs
    factorials[0] = 1
    for i in range(1, LIMIT + 1):
        factorials[i] = multiply_mod(factorials[i - 1], i)

    factorial_invs = [pow(x, MODULUS - 2, MODULUS) for x in factorials]

def solve(a, k):
    a.sort()

    result = 0
    for i in range(len(a)):
        result = add_mod(result, multiply_mod(a[i], multiply_mod(c_mod(i, k // 2), c_mod(len(a) - i - 1, k // 2))))

    return result

def c_mod(n, r):
    if n < r:
        return 0
    else:
        return multiply_mod(factorials[n], multiply_mod(factorial_invs[r], factorial_invs[n - r]))

def add_mod(x, y):
    return (x + y) % MODULUS

def multiply_mod(x, y):
    return (x * y) % MODULUS

if __name__ == "__main__":
    precompute()
    sc = int(input())
    for _ in range(sc):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, k))
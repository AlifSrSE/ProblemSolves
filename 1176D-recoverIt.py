# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1176/problem/D

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes

def get_largest_divisor(x, primes_set):
    if x in primes_set:
        return 1
    for i in range(int(x**0.5), 1, -1):
        if x % i == 0:
            return x // i
    return 1

def alif():
    n = int(input())
    b = list(map(int, input().split()))
    primes = sieve_of_eratosthenes(200000)
    primes_set = set(primes)
    b.sort(reverse=True)
    a = []
    used = [False] * (2 * n)
    prime_index_map = {p: i for i, p in enumerate(primes)}

    for i in range(2 * n):
        if used[i]:
            continue
        x = b[i]
        if x in primes_set:
            a.append(primes[x-1])
            used[i] = True
            used_prime_index = prime_index_map[x]
            for j in range(2*n):
                if not used[j] and b[j] == used_prime_index + 1:
                    used[j] = True
                    break
        else:
            divisor = get_largest_divisor(x, primes_set)
            a.append(x)
            used[i] = True
            for j in range(2 * n):
                if not used[j] and b[j] == divisor:
                    used[j] = True
                    break
    return " ".join(map(str, a))

if __name__ == "__main__":
    print(alif())
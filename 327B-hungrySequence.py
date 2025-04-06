# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

LIMIT = 2000000

def sieve(n):
    is_prime = [True] * (LIMIT + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for i in range(2, LIMIT + 1):
        if len(primes) >= n:
            break
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, LIMIT + 1, i):
                is_prime[j] = False

    return primes

def main():
    n = int(input())
    primes = sieve(n)
    print(" ".join(map(str, primes[:n])))

if __name__ == "__main__":
    main()

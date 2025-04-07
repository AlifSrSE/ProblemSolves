# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def sieve(n):
    if n < 6:
        limit = 13  
    else:
        import math
        limit = int(n * (math.log(n) + math.log(math.log(n))) + 10)
    
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for i in range(2, limit):
        if len(primes) >= n:
            break
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                is_prime[j] = False
    
    return primes[:n]

def main():
    n = int(input())
    primes = sieve(n)
    print(" ".join(map(str, primes)))

if __name__ == "__main__":
    main()

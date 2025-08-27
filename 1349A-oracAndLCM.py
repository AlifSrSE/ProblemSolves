# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from collections import defaultdict

def alif():
    def get_prime_factors(n):
        factors = defaultdict(int)
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] += 1
                n //= d
            d += 1
        if n > 1:
            factors[n] += 1
        return factors
    
    n_str = sys.stdin.readline()
    if not n_str:
        return
    
    n = int(n_str)
    a_str = sys.stdin.readline()

    if not a_str:
        return
    
    a = list(map(int, a_str.split()))
    prime_counts = defaultdict(list)
    
    for x in a:
        factors = get_prime_factors(x)
        for prime, count in factors.items():
            prime_counts[prime].append(count)
    result = 1
    
    for prime, counts in prime_counts.items():
        if len(counts) >= n - 1:
            counts.sort()
            if len(counts) == n:
                power = counts[1]
            else:
                power = counts[0]
            result *= (prime ** power)
            
    print(result)

if __name__ == "__main__":
    alif()
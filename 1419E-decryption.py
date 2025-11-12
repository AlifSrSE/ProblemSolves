# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import math
import sys
from collections import defaultdict

def get_divisors(n):
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if n > 1:
        divisors.append(n)
    return divisors

def alif():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        divisors = get_divisors(n)
        divisors.sort()
        
        if len(divisors) == 0:
            results.append(f"{n}")
            results.append("0")
            continue
            
        if len(divisors) == 1:
            results.append(f"{divisors[0]}")
            results.append("0")
            continue
            
        if len(divisors) == 2:
            results.append(f"{divisors[0]} {divisors[1]}")
            results.append("0")
            continue
        
        prime_factors = []
        temp = n
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                prime_factors.append(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            prime_factors.append(temp)
        
        if len(prime_factors) == 1:
            results.append(" ".join(map(str, divisors)))
            results.append("0")
            continue
        
        used = set()
        order = []
        
        for p in prime_factors:
            multiples = [d for d in divisors if d % p == 0 and d not in used]
            for d in multiples:
                if d not in used:
                    order.append(d)
                    used.add(d)
        
        remaining = [d for d in divisors if d not in used]
        for d in remaining:
            order.append(d)
            used.add(d)
        
        moves = 0
        for i in range(len(order) - 1):
            if math.gcd(order[i], order[i + 1]) == 1:
                moves += 1
        
        results.append(" ".join(map(str, order)))
        results.append(str(moves))
    
    print("\n".join(results))

if __name__ == "__main__":
    alif()
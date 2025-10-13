# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    n = int(sys.stdin.readline())
    
    if n == 1:
        print("C 1")
        sys.stdout.flush()
        return
    
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    result = 1
    idx = 0
    
    while idx < len(primes) and primes[idx] * primes[idx] <= n:
        p = primes[idx]
        print(f"B {p}")
        sys.stdout.flush()
        cnt = int(sys.stdin.readline())
        
        power = p
        while power * p <= n:
            print(f"B {power * p}")
            sys.stdout.flush()
            if int(sys.stdin.readline()) == 1:
                power *= p
            else:
                break
        
        if power > p:
            result *= power
        
        idx += 1
    
    if result == 1:
        large_primes = [p for p in primes if p * p > n]
        step = 100
        for i in range(0, len(large_primes), step):
            end = min(i + step, len(large_primes))
            for j in range(i, end):
                p = large_primes[j]
                print(f"B {p}")
                sys.stdout.flush()
                int(sys.stdin.readline())
            
            print("A 1")
            sys.stdout.flush()
            remaining = int(sys.stdin.readline())
            if remaining > n - (end - i):
                for j in range(i, end):
                    p = large_primes[j]
                    print(f"A {p}")
                    sys.stdout.flush()
                    if int(sys.stdin.readline()) == 1:
                        result = p
                        break
            if result != 1:
                break
    else:
        large_primes = [p for p in primes if p * p > n]
        for p in large_primes:
            print(f"B {p}")
            sys.stdout.flush()
            cnt = int(sys.stdin.readline())
            expected = n // p
            if cnt > expected - (1 if result % p == 0 else 0):
                result *= p
                break
    
    print(f"C {result}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
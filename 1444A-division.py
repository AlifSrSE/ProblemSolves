#Author: AlifSrSE

import sys

def solve(p, q):
    if p % q != 0:
        return p

    result = 0
    temp_q = q
    i = 2
    while i * i <= temp_q:
        if temp_q % i == 0:
            exponent = 0
            while temp_q % i == 0:
                exponent += 1
                temp_q //= i
            
            x = p
            while x % i == 0:
                x //= i
            for _ in range(exponent - 1):
                x *= i
            result = max(result, x)
        i += 1
    
    if temp_q != 1:
        x = p
        while x % temp_q == 0:
            x //= temp_q
        result = max(result, x)

    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        p = int(input_data[ptr])
        q = int(input_data[ptr+1])
        results.append(str(solve(p, q)))
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
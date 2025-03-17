# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1985/problem/G

MODULUS = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    index = 0
    t = data[index]
    index += 1
    
    for _ in range(t):
        l = data[index]
        r = data[index + 1]
        k = data[index + 2]
        index += 3
        
        print(solve(l, r, k))

def solve(l, r, k):
    return add_mod(compute_value_num(k, r), -compute_value_num(k, l))

def compute_value_num(k, limit):
    valid_digits = sum(1 for i in range(10) if i * k < 10)
    return pow_mod(valid_digits, limit)

def add_mod(x, y):
    return (x + y) % MODULUS

def multiply_mod(x, y):
    return (x * y) % MODULUS

def pow_mod(base, exponent):
    if exponent == 0:
        return 1
    
    result = pow_mod(multiply_mod(base, base), exponent // 2)
    if exponent % 2 == 1:
        result = multiply_mod(result, base)
    
    return result

if __name__ == "__main__":
    main()
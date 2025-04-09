# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def common_digits(a, b):
    digits = [False] * 10
    output = False
    while a > 0:
        digits[a % 10] = True
        a = a // 10
    while b > 0:
        if digits[b % 10]:
            output = True
            break
        b = b // 10
    return output

def main():
    n = int(input())
    total = 0
    divisors = []
    for k in range(1, int(math.sqrt(n)) + 1):
        if n % k == 0:
            divisors.append(k)
            if n // k > k:
                divisors.append(n // k)
    for k in range(len(divisors)):
        if common_digits(n, divisors[k]):
            total += 1
    print(total)

if __name__ == "__main__":
    main()
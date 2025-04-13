# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, b, c):
    mod_number = 1073741824
    max_prod = a * b * c
    divisors = [0] * (max_prod + 1)
    divisors[1] = 1
    for k in range(2, max_prod + 1):
        divisors[k] = 2
    for k in range(2, max_prod // 2 + 1):
        for m in range(2 * k, max_prod + 1, k):
            divisors[m] += 1
    total_sum = 0
    for first in range(1, a + 1):
        for second in range(1, b + 1):
            for third in range(1, c + 1):
                current_number = first * second * third
                total_sum += divisors[current_number]
                total_sum %= mod_number
    return total_sum

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
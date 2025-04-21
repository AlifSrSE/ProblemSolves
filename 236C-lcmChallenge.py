# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/236/problem/C

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def max_lcm_of_three(n):
    if n <= 2:
        return n
    if n == 3:
        return 6

    result = 0
    start = max(1, n - 10)

    for i in range(n, start - 1, -1):
        for j in range(i - 1, start - 1, -1):
            for k in range(j - 1, start - 1, -1):
                l = lcm(lcm(i, j), k)
                if l > result:
                    result = l

    return result

def main():
    n = int(input())
    print(max_lcm_of_three(n))

if __name__ == "__main__":
    main()


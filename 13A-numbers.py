# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/13/A

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def find_digit_sum(number, base):
    total = 0
    while number > 0:
        total += number % base
        number //= base
    return total

def solve():
    A = int(input())
    total_sum = 0
    for k in range(2, A):
        total_sum += find_digit_sum(A, k)
    
    current_gcd = gcd(total_sum, A - 2)
    print(f"{total_sum // current_gcd}/{ (A - 2) // current_gcd}")

solve()
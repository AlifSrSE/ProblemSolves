# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/469/problem/E

def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def find_range(a):
    l = 1
    r = 1
    current_sum = sum_of_digits(l)

    while current_sum % a != 0:
        r += 1
        current_sum += sum_of_digits(r)

    return l, r

a = int(input().strip())
l, r = find_range(a)

print(l, r)
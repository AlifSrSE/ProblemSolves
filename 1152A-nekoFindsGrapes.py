# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1152/problem/A

def read_array(size):
    return list(map(int, input().split()))

def count_even(arr):
    return sum(1 for x in arr if x % 2 == 0)

def alif(a, b):
    even_count_a = count_even(a)
    even_count_b = count_even(b)

    return min(even_count_a, len(b) - even_count_b) + min(len(a) - even_count_a, even_count_b)

# Input handling
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = read_array(n)
    b = read_array(m)
    print(alif(a, b))

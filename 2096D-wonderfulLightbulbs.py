# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/2096/problem/D

def process():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        readings = [tuple(map(int, input().split())) for _ in range(n)]

        xor_x = 0
        xor_sum_xy = 0

        for a, b in readings:
            xor_x ^= a
            xor_sum_xy ^= (a + b)

        value_s = xor_x
        value_t = xor_sum_xy - xor_x

        print(value_s, value_t)

if __name__ == "__main__":
    process()

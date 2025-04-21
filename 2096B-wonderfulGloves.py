# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/2096/problem/B

import sys
import threading

def process():
    input = sys.stdin.readline
    test_cases = int(input())
    
    for _ in range(test_cases):
        n, k = map(int, input().split())
        left = list(map(int, input().split()))
        right = list(map(int, input().split()))

        total_sum = 0
        adjustables = [0] * n

        for idx in range(n):
            a, b = left[idx], right[idx]
            if a >= b:
                total_sum += a
                adjustables[idx] = b
            else:
                total_sum += b
                adjustables[idx] = a

        adjustables.sort(reverse=True)
        add_on = sum(adjustables[:k - 1])
        result = total_sum + add_on + 1
        print(result)

if __name__ == "__main__":
    process()
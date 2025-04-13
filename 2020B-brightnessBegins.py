# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def compute_on_num(n):
    root = round(math.sqrt(n))
    if root * root > n:
        root -= 1
    return n - root

def solve(k):
    result = -1
    lower = 1
    upper = k * 2
    while lower <= upper:
        middle = (lower + upper) // 2
        if compute_on_num(middle) >= k:
            result = middle
            upper = middle - 1
        else:
            lower = middle + 1
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        print(solve(k))
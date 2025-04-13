# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    a, b = map(int, input().split())
    return max(0, a - max(0, b - a))

t = int(input())
for _ in range(t):
    print(solve())
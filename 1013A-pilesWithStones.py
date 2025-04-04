# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    return "Yes" if sum(x) >= sum(y) else "No"

print(solve())
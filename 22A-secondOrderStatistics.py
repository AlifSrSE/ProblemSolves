# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/22/A

def solve():
    current_min = float('inf')
    second_min = float('inf')
    n = int(input())

    nums = list(map(int, input().split()))

    for temp in nums:
        if temp < current_min:
            second_min = current_min
            current_min = temp
        elif current_min < temp < second_min:
            second_min = temp

    if second_min == float('inf'):
        print("NO")
    else:
        print(second_min)

solve()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/2049/A

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        s = 0
        prev = False
        for x in nums:
            if x:
                s += not prev
                prev = True
            else:
                s += prev
                prev = False

        if s == 0:
            print("0")
        elif s <= 2:
            print("1")
        else:
            print("2")

solve()
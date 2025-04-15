# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/1/A

def solve():
    length, width, stone = map(int, input().split())
    num_stones = (length // stone + (length % stone > 0)) * (width // stone + (width % stone > 0))
    print(num_stones)

solve()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    weights = list(map(int, input().split()))

    ones = weights.count(100)
    twos = weights.count(200)

    possible = True
    if ones % 2 == 1:
        possible = False
    elif twos % 2 == 1 and ones < 2:
        possible = False

    print("YES" if possible else "NO")

solve()
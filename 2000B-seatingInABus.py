# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    n = len(a)
    occupied = [False] * n

    for i in range(n):
        if i != 0 and (
            (a[i] == 1 or not occupied[a[i] - 2]) and
            (a[i] == n or not occupied[a[i]])
        ):
            return False
        occupied[a[i] - 1] = True

    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if solve(a) else "NO")

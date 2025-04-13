# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        first, second = map(int, input().split())
        a.append((first, second))

    def cmp(item):
        first, second = item
        return (min(first, second), max(first, second), first)

    a.sort(key=cmp)

    for first, second in a:
        print(first, second, end=" ")
    print()

t = int(input())
for _ in range(t):
    solve()
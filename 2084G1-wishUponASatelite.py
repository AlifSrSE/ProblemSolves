# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    zeros_count = a.count(0)
    present_numbers = sorted([x for x in a if x != 0])
    missing_numbers = sorted(list(set(range(1, n + 1)) - set(present_numbers)))

    def calculate_f(arr):
        m = len(arr)
        if m == 1:
            return arr[0]
        return arr[0] if m % 2 == 1 else min(arr[0], arr[-1])

    def calculate_beauty(perm):
        beauty = 0
        for i in range(n):
            for j in range(i, n):
                subsegment = perm[i : j + 1]
                beauty += calculate_f(list(subsegment))
        return beauty

    import itertools

    max_beauty = 0
    possible_fills = list(itertools.permutations(missing_numbers))

    for fill in possible_fills:
        temp_perm = list(a)
        fill_idx = 0
        for i in range(n):
            if temp_perm[i] == 0:
                temp_perm[i] = fill[fill_idx]
                fill_idx += 1
        max_beauty = max(max_beauty, calculate_beauty(tuple(temp_perm)))

    print(max_beauty)


t = int(input())
for _ in range(t):
    solve()
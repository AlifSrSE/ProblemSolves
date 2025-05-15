# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/276/C

def solve():
    n, q = map(int, input().split())
    array = [0] + list(map(int, input().split()))
    times = [0] * (n + 1)

    for _ in range(q):
        left, right = map(int, input().split())
        times[left] += 1
        if right < n:
            times[right + 1] -= 1

    for k in range(2, n + 1):
        times[k] += times[k - 1]

    array.sort()
    times.sort()

    total = 0
    for k in range(1, n + 1):
        total += times[k] * array[k]

    print(total)

if __name__ == "__main__":
    solve()
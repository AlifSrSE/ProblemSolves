
import sys

def solve(a, x):
    result = 0
    n = len(a)

    for i in range(n):
        is_sorted = True
        for j in range(max(1, i), n):
            if a[j] < a[j-1]:
                is_sorted = False
                break

        if is_sorted:
            return result

        if a[i] > x:
            a[i], x = x, a[i]
            result += 1

        if i > 0 and a[i] < a[i-1]:
            return -1

    return result if all(a[i] <= a[i+1] for i in range(n-1)) else -1


t = int(sys.stdin.readline())
for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a, x))
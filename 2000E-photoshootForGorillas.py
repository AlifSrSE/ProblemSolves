# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def compute_freq(k, length, position):
    return min(length - k, position) - max(0, position - k + 1) + 1

def solve(n, m, k, a):
    freqs = []
    for r in range(n):
        for c in range(m):
            freqs.append(compute_freq(k, n, r) * compute_freq(k, m, c))
    freqs.sort(reverse=True)  

    heights = a[:n * m] + [0] * max(0, n * m - len(a))
    heights.sort(reverse=True)

    return sum(h * f for h, f in zip(heights, freqs))

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    w = int(input())
    a = list(map(int, input().split()))
    print(solve(n, m, k, a))

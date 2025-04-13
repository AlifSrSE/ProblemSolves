# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, x):
    counts = [0] * (len(a) + 1)
    for ai in a:
        if ai < len(counts):
            counts[ai] += 1
    result = 0
    while counts[result] != 0:
        if result + x < len(counts):
            counts[result + x] += counts[result] - 1
        result += 1
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, x))
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1163/problem/B2

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    counts = {}
    res = 0
    for p in range(n):
        col = a[p]
        counts[col] = counts.get(col, 0) + 1
        length = p + 1
        distinct_count = len(counts)
        frequencies = sorted(counts.values())

        if distinct_count == 1:
            res = length
        elif distinct_count == length:
            res = length
        elif (len(frequencies) > 1 and frequencies[0] == 1 and all(f == frequencies[1] for f in frequencies[1:])):
            res = length
        elif (len(frequencies) > 1 and frequencies[-1] == frequencies[0] + 1 and all(f == frequencies[0] for f in frequencies[:-1])):
            res = length

    print(res)

if __name__ == "__main__":
    alif()
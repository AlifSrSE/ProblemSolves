# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1215/problem/A

def alif():
    import sys
    input_values = []
    while len(input_values) < 5:
        input_values += list(map(int, sys.stdin.readline().split()))
    a1, a2, k1, k2, n = input_values

    min_games_without_prize = (k1 - 1) * a1 + (k2 - 1) * a2

    mn = max(0, n - min_games_without_prize)

    if k1 < k2:
        kx, ax = k1, a1
        ky, ay = k2, a2
    else:
        kx, ax = k2, a2
        ky, ay = k1, a1

    mx = 0
    if n >= ax * kx:
        mx += ax
        n -= ax * kx
        mx += min(n // ky, ay)
    else:
        mx = n // kx

    print(mn, mx)

if __name__ == "__main__":
    alif()
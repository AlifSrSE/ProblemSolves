# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1153/problem/B

def read_array():
    return list(map(int, input().split()))

def alif(h, a, b, height):
    n = len(h)
    m = len(h[0])

    heights = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            heights[i][j] = 0 if h[i][j] == 0 else min(a[j], b[i])

    return '\n'.join(' '.join(map(str, row)) for row in heights)

if __name__ == "__main__":
    n, m, height = map(int, input().split())
    a = read_array()
    b = read_array()
    h = [read_array() for _ in range(n)]

    print(alif(h, a, b, height))

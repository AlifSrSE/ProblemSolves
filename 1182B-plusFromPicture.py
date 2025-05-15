# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1182/problem/B

R_OFFSETS = [-1, 0, 1, 0]
C_OFFSETS = [0, 1, 0, -1]

def alif(cells):
    h = len(cells)
    w = len(cells[0])

    star_count = sum(row.count('*') for row in cells)

    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if (cells[r][c] == '*' and
                cells[r - 1][c] == '*' and
                cells[r][c - 1] == '*' and
                cells[r + 1][c] == '*' and
                cells[r][c + 1] == '*'):
                covered_count = compute_covered_count(cells, r, c)
                if covered_count == star_count:
                    return "YES"
    return "NO"

def compute_covered_count(cells, r, c):
    return sum(compute_ray_length(cells, r, c, R_OFFSETS[i], C_OFFSETS[i]) for i in range(len(R_OFFSETS))) + 1

def compute_ray_length(cells, r, c, offset_r, offset_c):
    h = len(cells)
    w = len(cells[0])
    result = 0
    while True:
        r += offset_r
        c += offset_c
        if 0 <= r < h and 0 <= c < w and cells[r][c] == '*':
            result += 1
        else:
            return result

if __name__ == "__main__":
    h = int(input())
    w = int(input())
    cells = [list(input()) for _ in range(h)]
    print(alif(cells))

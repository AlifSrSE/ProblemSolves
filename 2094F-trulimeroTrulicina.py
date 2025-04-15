# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def generate_grid(n, m, k):
    grid = [[0]*m for _ in range(n)]
    if m % k != 0:
        for i in range(n):
            for j in range(m):
                grid[i][j] = (i * m + j) % k + 1
    elif n % k != 0:
        for j in range(m):
            for i in range(n):
                grid[i][j] = (j * n + i) % k + 1
    else:
        for i in range(n):
            for j in range(m):
                grid[i][j] = (i + j) % k + 1
    return grid

def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        grid = generate_grid(n, m, k)
        for row in grid:
            print(*row)

if __name__ == "__main__":
    main()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1162/problem/B

def alif():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))

    for row in range(n):
        for col in range(m):
            x = a[row][col]
            y = b[row][col]
            a[row][col] = min(x, y)
            b[row][col] = max(x, y)

    possible = True
    for row in range(n):
        for col in range(m):
            if (row > 0 and a[row][col] <= a[row - 1][col]) or \
               (col > 0 and a[row][col] <= a[row][col - 1]):
                possible = False
            if (row > 0 and b[row][col] <= b[row - 1][col]) or \
               (col > 0 and b[row][col] <= b[row][col - 1]):
                possible = False

    if possible:
        print("Possible")
    else:
        print("Impossible")

if __name__ == "__main__":
    alif()
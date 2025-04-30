# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1162/problem/A

def alif():
    n, h, m = map(int, input().split())
    l = [0] * m
    r = [0] * m
    x = [0] * m
    for i in range(m):
        l[i], r[i], x[i] = map(int, input().split())

    heights = [h] * n
    for i in range(m):
        for j in range(l[i] - 1, r[i]):
            heights[j] = min(heights[j], x[i])

    total_squared_height = sum(height ** 2 for height in heights)
    print(total_squared_height)

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2056/problem/B

def solve(g):
    n = len(g)
    result = [0] * n

    for i in range(n):
        sequence = 0
        for j in range(i + 1, n):
            if g[i][j] == 0:
                sequence += 1

        index = 0
        while True:
            while result[index] != 0:
                index += 1

            if sequence == 0:
                result[index] = i + 1
                break

            index += 1
            sequence -= 1

    return " ".join(map(str, result))

t = int(input())
for _ in range(t):
    n = int(input())
    g = []
    for _ in range(n):
        line = input()
        g.append([int(char) for char in line])
    print(solve(g))
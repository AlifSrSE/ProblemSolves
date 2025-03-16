import sys

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    a = [0] + a  # 1-indexed
    mn = min(a[1:])
    tot = 0
    X = [[] for _ in range(3 * n + 1)]
    Y = [[] for _ in range(3 * n + 1)]

    p1 = 0
    for i in range(1, n + 1):
        if a[i] == mn:
            p1 = i
            break

    if p1 != 1:
        tot += 1
        for i in range(1, p1 + 1):
            X[tot].append(1)
            Y[tot].append(i)
            a[1], a[i] = a[i], a[1]
        for i in range(2, p1 + 1):
            X[tot].append(i)
            Y[tot].append(p1)
            a[i], a[p1] = a[p1], a[i]
        for i in range(p1 + 1, n + 1):
            X[tot].append(p1)
            Y[tot].append(i)
            a[p1], a[i] = a[i], a[p1]
        for i in range(p1 + 1, n + 1):
            X[tot].append(i)
            Y[tot].append(n)
            a[i], a[n] = a[n], a[i]

    def walk1(j):
        X[tot].append(j - 1)
        Y[tot].append(j)
        X[tot].append(j - 1)
        Y[tot].append(j + 1)
        X[tot].append(j)
        Y[tot].append(j + 1)
        X[tot].append(j + 1)
        Y[tot].append(j + 1)
        a[j - 1], a[j + 1] = a[j + 1], a[j - 1]

    def walk2(j):
        X[tot].append(j - 1)
        Y[tot].append(j)
        X[tot].append(j)
        Y[tot].append(j)
        X[tot].append(j)
        Y[tot].append(j + 1)
        X[tot].append(j + 1)
        Y[tot].append(j + 1)
        a[j - 1], a[j] = a[j], a[j - 1]
        a[j], a[j + 1] = a[j + 1], a[j]

    def path2():
        nonlocal tot
        tot += 1
        for i in range(1, n + 1):
            X[tot].append(1)
            Y[tot].append(i)
            a[1], a[i] = a[i], a[1]
        for i in range(2, n + 1):
            X[tot].append(i)
            Y[tot].append(n)
            a[i], a[n] = a[n], a[i]

    for i in range(2, n + 1):
        tot += 1
        X[tot].append(1)
        Y[tot].append(1)
        if n % 2 == 1:
            if i % 2 == 1:
                j = 2
                while j <= n:
                    if j + 1 == i:
                        walk2(j)
                    elif a[j] > a[j + 1]:
                        walk1(j)
                    else:
                        walk2(j)
                    j += 2
            else:
                j = 2
                while j <= n:
                    if a[j] > a[j + 1]:
                        walk1(j)
                    else:
                        walk2(j)
                    j += 2
        else:
            if i % 2 == 1:
                j = 2
                while j <= n:
                    if j == i - 1:
                        X[tot].append(j - 1)
                        Y[tot].append(j)
                        X[tot].append(j)
                        Y[tot].append(j)
                        a[j - 1], a[j] = a[j], a[j - 1]
                        j -= 1
                    elif a[j] > a[j + 1]:
                        walk1(j)
                    else:
                        walk2(j)
                    j += 2
            else:
                j = 2
                while j <= n:
                    if j == i:
                        X[tot].append(j - 1)
                        Y[tot].append(j)
                        X[tot].append(j)
                        Y[tot].append(j)
                        a[j - 1], a[j] = a[j], a[j - 1]
                        j -= 1
                    elif a[j] > a[j + 1]:
                        walk1(j)
                    else:
                        walk2(j)
                    j += 2
        path2()

    print(tot)
    for i in range(1, tot + 1):
        result = ""
        for j in range(1, 2 * n - 1):
            if X[i][j] == X[i][j - 1]:
                result += "R"
            else:
                result += "D"
        print(result)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    solve()
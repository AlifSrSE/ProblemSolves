import sys

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    a = [0] + a  # 1-indexed
    tot = 0
    X = [[] for _ in range(3 * n + 1)]
    Y = [[] for _ in range(3 * n + 1)]

    def path3(num, p):
        nonlocal tot
        for i in range(1, p[0] + 1):
            X[num].append(1)
            Y[num].append(i)
            a[1], a[i] = a[i], a[1]
        for i in range(1, len(p)):
            for j in range(p[i - 1], p[i] + 1):
                X[num].append(i + 1)
                Y[num].append(j)
                a[i + 1], a[j] = a[j], a[i + 1]
        x = len(p)
        y = p[-1]
        while x != n:
            x += 1
            X[num].append(x)
            Y[num].append(y)
            a[x], a[y] = a[y], a[x]
        while y != n:
            y += 1
            X[num].append(x)
            Y[num].append(y)
            a[x], a[y] = a[y], a[x]

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

    def walk3(j):
        X[tot].append(j - 1)
        Y[tot].append(j)
        X[tot].append(j)
        Y[tot].append(j)
        a[j - 1], a[j] = a[j], a[j - 1]

    def init():
        nonlocal tot, a
        pr = []
        for i in range(1, n + 1):
            pr.append((a[i], i))
        pr.sort()
        for i in range(1, n + 1):
            a[pr[i - 1][1]] = i
        tot = 0
        for i in range(1, 3 * n + 1):
            X[i].clear()
            Y[i].clear()

    def step1():
        nonlocal tot
        p1, pn = 0, 0
        p = []
        for i in range(1, n + 1):
            if a[i] == 1:
                p1 = i
                break
        if p1 != 1:
            p.append(p1)
            path3(tot + 1, p)
            tot += 1
        if n == 2:
            return
        tot += 1
        X[tot].append(1)
        Y[tot].append(1)
        j = 2
        while j <= n:
            if j + 1 > n:
                walk3(j)
            elif a[j] == n:
                walk1(j)
            else:
                walk2(j)
            j += 2
        p1 = n
        for i in range(1, n + 1):
            if a[i] == n:
                pn = i
                break
        p.clear()
        p.append(pn)
        p.append(p1)
        path3(tot + 1, p)
        tot += 1
        p.clear()
        for i in range(1, n + 1):
            if a[i] <= (n + 1) // 2:
                p.append(i)
        path3(tot + 1, p)
        tot += 1

    def step2():
        nonlocal tot
        head = 0
        if n % 2 == 1:
            for t in range(1, 3):
                head = n // 2 + 2
                for i in range(1, n // 2 + (1 if t == 1 else 0) + 1):
                    tot += 1
                    X[tot].append(1)
                    Y[tot].append(1)
                    for j in range(2, n + 1):
                        if not (head <= j <= head + n // 2 - 1):
                            walk3(j)
                        elif j == head and head % 2 == 1:
                            walk3(j)
                        else:
                            if not (head <= j + 1 <= head + n // 2 - 1):
                                walk3(j)
                            elif a[j] > a[j + 1]:
                                walk1(j)
                                j += 1
                            else:
                                walk2(j)
                                j += 1
                    head -= 1
        else:
            for t in range(1, 3):
                head = n // 2 + 1
                for i in range(1, n // 2 + 1):
                    tot += 1
                    X[tot].append(1)
                    Y[tot].append(1)
                    for j in range(2, n + 1):
                        if not (head <= j <= head + n // 2 - 1):
                            walk3(j)
                        elif j == head and head % 2 == 1:
                            walk3(j)
                        else:
                            if not (head <= j + 1 <= head + n // 2 - 1):
                                walk3(j)
                            elif a[j] > a[j + 1]:
                                walk1(j)
                                j += 1
                            else:
                                walk2(j)
                                j += 1
                    head -= 1

    def output():
        print(tot)
        for i in range(1, tot + 1):
            result = ""
            for j in range(1, 2 * n - 1):
                if X[i][j] == X[i][j - 1]:
                    result += "R"
                else:
                    result += "D"
            print(result)

    init()
    step1()
    step2()
    output()

T = int(sys.stdin.readline().strip())
for _ in range(T):
    solve()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/19/A

def solve():
    n = int(input())
    m = {}
    for _ in range(n):
        s = input()
        m[s] = {'name': s, 'pts': 0, 'diff': 0, 'scored': 0}

    for _ in range(n * (n - 1) // 2):
        names, goals = input().split()
        xn, yn = "", ""
        dash = False
        for p in range(len(names)):
            if names[p] == '-':
                dash = True
            elif dash:
                yn += names[p]
            else:
                xn += names[p]

        xg, yg = 0, 0
        colon = False
        for p in range(len(goals)):
            if goals[p] == ':':
                colon = True
            elif colon:
                yg = 10 * yg + (ord(goals[p]) - ord('0'))
            else:
                xg = 10 * xg + (ord(goals[p]) - ord('0'))

        m[xn]['scored'] += xg
        m[yn]['scored'] += yg
        m[xn]['diff'] += xg - yg
        m[yn]['diff'] += yg - xg
        if xg > yg:
            m[xn]['pts'] += 3
        elif xg < yg:
            m[yn]['pts'] += 3
        else:
            m[xn]['pts'] += 1
            m[yn]['pts'] += 1

    v = list(m.values())
    v.sort(key=lambda x: (-x['pts'], -x['diff'], -x['scored']))

    res = [v[p]['name'] for p in range(n // 2)]
    res.sort()
    for p in range(len(res)):
        print(res[p])

solve()
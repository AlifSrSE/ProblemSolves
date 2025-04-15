# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/18/A

def is_right(c):
    sides = [0] * 3
    sides[0] = (c[4] - c[2]) * (c[4] - c[2]) + (c[5] - c[3]) * (c[5] - c[3])
    sides[1] = (c[4] - c[0]) * (c[4] - c[0]) + (c[5] - c[1]) * (c[5] - c[1])
    sides[2] = (c[2] - c[0]) * (c[2] - c[0]) + (c[3] - c[1]) * (c[3] - c[1])

    sides.sort()
    if sides[0] > 0 and sides[2] == sides[0] + sides[1]:
        return True
    else:
        return False

def solve():
    points = list(map(int, input().split()))

    output = "NEITHER"
    if is_right(points):
        output = "RIGHT"
    else:
        for k in range(6):
            points[k] += 1
            if is_right(points):
                output = "ALMOST"
                break
            points[k] -= 2
            if is_right(points):
                output = "ALMOST"
                break
            points[k] += 1

    print(output)

solve()
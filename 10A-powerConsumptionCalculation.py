# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/10/A

def solve():
    n, P1, P2, P3, T1, T2 = map(int, input().split())
    total = 0
    previous_time = -1

    for _ in range(n):
        start, finish = map(int, input().split())
        if previous_time < 0:
            previous_time = start
        total += P1 * (finish - start)

        time_idle = start - previous_time
        if time_idle > T1 + T2:
            total += (time_idle - T1 - T2) * P3
            time_idle = T1 + T2
        if time_idle > T1:
            total += (time_idle - T1) * P2
            time_idle = T1
        total += time_idle * P1

        previous_time = finish

    print(total)

solve()
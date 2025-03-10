# Author : AlifSrSE
# Date : 2025-02-16
# Problem link : https://codeforces.com/contest/469/problem/B

def count_suitable_times(p_intervals, q_intervals, l, r):
    suitable_times = 0
    for t in range(l, r + 1):
        for (c, d) in q_intervals:
            shifted_interval = (c + t, d + t)
            for (a, b) in p_intervals:
                if not (shifted_interval[1] < a or shifted_interval[0] > b):
                    suitable_times += 1
                    break
            else:
                continue
            break
    return suitable_times

p, q, l, r = map(int, input().split())
p_intervals = [tuple(map(int, input().split())) for _ in range(p)]
q_intervals = [tuple(map(int, input().split())) for _ in range(q)]

print(count_suitable_times(p_intervals, q_intervals, l, r))
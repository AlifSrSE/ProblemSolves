#Author: AlifSrSE

import sys

def solve(t):
    t.sort()
    n = len(t)
    max_time = 2 * n + 1
    dp = [abs(i - t[0]) for i in range(max_time)]
    dp[0] = float('inf')

    for i in range(1, n):
        next_dp = [float('inf')] * max_time
        min_prev = dp[1]
        for j in range(2, max_time):
            next_dp[j] = min_prev + abs(j - t[i])
            min_prev = min(min_prev, dp[j])
        dp = next_dp

    return int(min(dp))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(q):
        n = int(input_data[ptr])
        t_arr = [int(x) for x in input_data[ptr+1 : ptr+1+n]]
        results.append(str(solve(t_arr)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
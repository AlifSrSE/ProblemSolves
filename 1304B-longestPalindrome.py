# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1304/problem/B

import sys
from collections import defaultdict

def alif():
    sys.stdin.readline
    try:
        n, m = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return
    counts = defaultdict(int)

    for _ in range(n):
        s = sys.stdin.readline().strip()
        counts[s] += 1
    f_parts = []
    g_parts = []
    middle_part = ""
    sorted_unique_strings = sorted(counts.keys())

    for s in sorted_unique_strings:
        rev_s = s[::-1]

        if s == rev_s:
            if counts[s] > 0:
                if counts[s] % 2 == 1:
                    if not middle_part:
                        middle_part = s
                    num_pairs = counts[s] // 2
                    for _ in range(num_pairs):
                        f_parts.append(s)
                        g_parts.append(rev_s)
                else:
                    num_pairs = counts[s] // 2
                    for _ in range(num_pairs):
                        f_parts.append(s)
                        g_parts.append(rev_s)
            continue
        
        if counts[s] > 0 and counts[rev_s] > 0:
            num_pairs = min(counts[s], counts[rev_s])
            for _ in range(num_pairs):
                f_parts.append(s)
                g_parts.append(rev_s)
            counts[s] -= num_pairs
            counts[rev_s] -= num_pairs

    result_f = "".join(f_parts)
    result_g = "".join(g_parts)
    result_g_reversed = "".join(reversed(g_parts))
    final_result = result_f + middle_part + result_g_reversed
    print(len(final_result))
    print(final_result)

if __name__ == "__main__":
    alif()
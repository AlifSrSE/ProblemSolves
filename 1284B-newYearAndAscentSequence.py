# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1284/problem/B

import sys
from bisect import bisect_right

def alif():
    try:
        n = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    min_vals = []
    max_vals = []
    sequences_with_ascent_count = 0
    
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        l = line[0]
        s = line[1:]
        has_ascent = False
        if l > 1:
            for i in range(1, l):
                if s[i] > s[i-1]:
                    has_ascent = True
                    break
        
        if has_ascent:
            sequences_with_ascent_count += 1
        else:
            min_vals.append(s[-1])
            max_vals.append(s[0])

    sequences_without_ascent_count = n - sequences_with_ascent_count
    max_vals.sort()
    no_ascent_bad_pairs = 0

    for min_val in min_vals:
        count = bisect_right(max_vals, min_val)
        no_ascent_bad_pairs += count

    total_pairs = n * n
    pairs_with_no_ascent = no_ascent_bad_pairs
    ans = total_pairs - pairs_with_no_ascent
    print(ans)

if __name__ == "__main__":
    alif()
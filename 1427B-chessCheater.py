#Author: AlifSrSE

import sys

def solve(s, k):
    l_count = s.count('L')
    k = min(k, l_count)
    
    if l_count == len(s):
        return 0 if k == 0 else (2 * k - 1)

    initial_score = 0
    for i in range(len(s)):
        if s[i] == 'W':
            if i > 0 and s[i-1] == 'W':
                initial_score += 2
            else:
                initial_score += 1
    
    result = initial_score + (k * 2)

    gaps = []
    win_found = False
    gap = 0
    for c in s:
        if c == 'W':
            if gap != 0 and win_found:
                gaps.append(gap)
            gap = 0
            win_found = True
        else:
            gap += 1
            
    gaps.sort()
    for g in gaps:
        if k >= g:
            k -= g
            result += 1
            
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        ptr += 1 # skip n
        k = int(input_data[ptr])
        s = input_data[ptr + 1]
        results.append(str(solve(s, k)))
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
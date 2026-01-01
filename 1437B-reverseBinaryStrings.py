#Author: AlifSrSE

import sys

def compute_min_oper_num(s, target_at_even_index):
    matched = []
    for i in range(len(s)):
        matched.append((i % 2 == 0) == (s[i] == target_at_even_index))
    
    count = 0
    for i in range(len(matched)):
        if not matched[i] and (i == 0 or matched[i-1]):
            count += 1
    return count

def solve(s):
    return min(compute_min_oper_num(s, '0'), compute_min_oper_num(s, '1'))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    
    results = []
    for _ in range(t):
        ptr += 1 # skip n
        s = input_data[ptr]
        results.append(str(solve(s)))
        ptr += 1
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
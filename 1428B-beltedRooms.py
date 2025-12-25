#Author: AlifSrSE

import sys

def solve(s):
    n = len(s)
    all_right = all(ch == '-' or ch == '>' for ch in s)
    all_left = all(ch == '-' or ch == '<' for ch in s)
    
    if all_right or all_left:
        return n

    count = 0
    for i in range(n):
        if s[i] == '-' or s[(i + 1) % n] == '-':
            count += 1
    return count

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        s = input_data[ptr + 1]
        results.append(str(solve(s)))
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
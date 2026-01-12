#Author: AlifSrSE

import sys

def solve(a, b, map_str):
    INF = 10000
    result = 0
    prev_index = -INF
    # Count first segment cost
    found_first = False
    for i in range(len(map_str)):
        if map_str[i] == '1':
            if not found_first:
                result += a
                found_first = True
            else:
                result += min(a, b * (i - prev_index - 1))
            prev_index = i
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        a = int(input_data[ptr])
        b = int(input_data[ptr+1])
        map_str = input_data[ptr+2]
        results.append(str(solve(a, b, map_str)))
        ptr += 3
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
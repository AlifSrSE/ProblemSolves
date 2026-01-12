#Author: AlifSrSE

import sys

def solve(s, c0, c1, h):
    result = 0
    for ch in s:
        if (ch == '0' and c1 + h < c0) or (ch == '1' and c0 + h < c1):
            result += h
            ch = '1' if ch == '0' else '0'
        result += c0 if ch == '0' else c1
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
        c0 = int(input_data[ptr])
        c1 = int(input_data[ptr+1])
        h = int(input_data[ptr+2])
        s = input_data[ptr+3]
        results.append(str(solve(s, c0, c1, h)))
        ptr += 4
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
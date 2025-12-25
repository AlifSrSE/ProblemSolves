#Author: AlifSrSE

import sys

def solve(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) + (2 if x1 != x2 and y1 != y2 else 0)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        x1 = int(input_data[ptr])
        y1 = int(input_data[ptr+1])
        x2 = int(input_data[ptr+2])
        y2 = int(input_data[ptr+3])
        results.append(str(solve(x1, y1, x2, y2)))
        ptr += 4
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
# Author: AlifSrSE
import sys

def solve(bottoms, lefts):
    bottom_set = set(bottoms)
    count = 0
    for x in lefts:
        if x in bottom_set:
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
        m = int(input_data[ptr + 1])
        bottoms = input_data[ptr + 2 : ptr + 2 + n]
        lefts = input_data[ptr + 2 + n : ptr + 2 + n + m]
        results.append(str(solve(bottoms, lefts)))
        ptr += 2 + n + m
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
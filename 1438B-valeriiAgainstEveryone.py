#Author: AlifSrSE

import sys

def solve(b):
    return len(set(b)) != len(b)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        b = [int(x) for x in input_data[ptr+1 : ptr+1+n]]
        results.append("YES" if solve(b) else "NO")
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
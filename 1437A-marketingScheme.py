#Author: AlifSrSE

import sys

def solve(l, r):
    return l * 2 >= r + 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        l = int(input_data[ptr])
        r = int(input_data[ptr+1])
        results.append("YES" if solve(l, r) else "NO")
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
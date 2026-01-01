#Author: AlifSrSE

import sys

def solve(a, m):
    return sum(a) == m

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1])
        a = [int(x) for x in input_data[ptr+2 : ptr+2+n]]
        results.append("YES" if solve(a, m) else "NO")
        ptr += 2 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()

    
#Author: AlifSrSE

import sys

def solve(x):
    s = str(x)
    return 10 * (ord(s[0]) - ord('0') - 1) + len(s) * (len(s) + 1) // 2

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        x = int(input_data[i])
        results.append(str(solve(x)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
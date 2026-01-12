#Author: AlifSrSE

import sys

def solve(n):
    return " ".join(str(4 * n - 2 * i) for i in range(n))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = [solve(int(input_data[i])) for i in range(1, t + 1)]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
# Author: AlifSrSE
import sys

def solve(x, y):
    common = min(x, y)
    return common * 2 + max(0, 2 * (x + y - common * 2) - 1)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        x = int(input_data[ptr])
        y = int(input_data[ptr + 1])
        results.append(str(solve(x, y)))
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
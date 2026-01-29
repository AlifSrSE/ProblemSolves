# Author: AlifSrSE
import sys

def solve(a):
    n = len(a)
    if n == 0: return 0
    max_val = max(a)
    total_sum = sum(a)

    result = max_val * (n - 1) - total_sum
    if result < 0:
        result = (result % (n - 1) + (n - 1)) % (n - 1)
    
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        a = [int(x) for x in input_data[ptr + 1 : ptr + 1 + n]]
        results.append(str(solve(a)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
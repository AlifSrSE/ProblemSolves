#Author: AlifSrSE

import sys

def solve(n, k, a):
    a.sort()
    result = 0
    index = len(a) - 1 - n // 2
    for _ in range(k):
        result += a[index]
        index -= (1 + n // 2)
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
        k = int(input_data[ptr+1])
        a = [int(x) for x in input_data[ptr+2 : ptr+2 + n*k]]
        results.append(str(solve(n, k, a)))
        ptr += 2 + n*k
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
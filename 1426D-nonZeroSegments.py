#Author: AlifSrSE

import sys

def solve(a):
    result = 0
    sums = set()
    current_sum = 0
    for ai in a:
        current_sum += ai
        if current_sum == 0 or current_sum in sums:
            result += 1
            sums = set()
            sums.add(ai)
            current_sum = ai
        else:
            sums.add(current_sum)
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    print(solve(a))

if __name__ == "__main__":
    main()
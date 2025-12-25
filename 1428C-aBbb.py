#Author: AlifSrSE

import sys

def solve(s):
    stack = []
    for ch in s:
        if ch == 'B' and stack:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        results.append(str(solve(s)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
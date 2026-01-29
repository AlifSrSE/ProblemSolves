
# Author: AlifSrSE
import sys

def solve(s):
    result = 0
    curve_count = 0
    square_count = 0
    for ch in s:
        if ch == '(':
            curve_count += 1
        elif ch == ')':
            if curve_count != 0:
                result += 1
                curve_count -= 1
        elif ch == '[':
            square_count += 1
        elif ch == ']':
            if square_count != 0:
                result += 1
                square_count -= 1
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = [str(solve(s)) for s in input_data[1 : t + 1]]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
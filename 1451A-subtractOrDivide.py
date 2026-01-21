
# Author: AlifSrSE
import sys

def solve(n):
    if n <= 3:
        return n - 1
    return 2 if n % 2 == 0 else 3

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = [str(solve(int(n))) for n in input_data[1:t+1]]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
# Author: AlifSrSE
import sys

def solve(n):
    return " ".join(str((i + 1) % n + 1) for i in range(n))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    t = int(input_data[0])
    results = [solve(int(n)) for n in input_data[1:t+1]]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()

    
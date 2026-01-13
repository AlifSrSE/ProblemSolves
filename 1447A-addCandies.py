

#Author: AlifSrSE

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(f"{n}\n{' '.join(map(str, range(1, n + 1)))}")
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
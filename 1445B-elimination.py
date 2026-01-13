#Author: AlifSrSE

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        a = int(input_data[ptr])
        b = int(input_data[ptr + 1])
        c = int(input_data[ptr + 2])
        d = int(input_data[ptr + 3])
        ptr += 4
        results.append(str(max(a + b, c + d)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
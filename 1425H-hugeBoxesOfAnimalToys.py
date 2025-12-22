#Author: AlifSrSE

import sys

def solve(A, B, C, D):
    if (A + B) % 2 == 0:
        opt1 = "Tidak" if (B + C == 0) else "Ya"
        opt2 = "Tidak" if (A + D == 0) else "Ya"
        return f"Tidak Tidak {opt1} {opt2}"
    else:
        opt1 = "Tidak" if (A + D == 0) else "Ya"
        opt2 = "Tidak" if (B + C == 0) else "Ya"
        return f"{opt1} {opt2} Tidak Tidak"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(T):
        A = int(input_data[ptr])
        B = int(input_data[ptr+1])
        C = int(input_data[ptr+2])
        D = int(input_data[ptr+3])
        results.append(solve(A, B, C, D))
        ptr += 4
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
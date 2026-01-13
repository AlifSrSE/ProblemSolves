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
        n = int(input_data[ptr])
        x = int(input_data[ptr + 1])
        ptr += 2
        a = [int(i) for i in input_data[ptr:ptr + n]]
        ptr += n
        b = [int(i) for i in input_data[ptr:ptr + n]]
        ptr += n
        
        a.sort()
        b.sort(reverse=True)
        
        possible = True
        for i in range(n):
            if a[i] + b[i] > x:
                possible = False
                break
        results.append("Yes" if possible else "No")
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
# Author: AlifSrSE
import sys

def solve(d, k):
    a = 0
    while 2 * (a + k)**2 <= d**2:
        a += k
        
    if a**2 + (a + k)**2 <= d**2:
        return "Ashish"
    else:
        return "Utkarsh"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        d = int(input_data[ptr])
        k = int(input_data[ptr+1])
        ptr += 2
        results.append(solve(d, k))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
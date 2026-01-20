# Author: AlifSrSE

import sys

def solve(a):
    return "".join(sorted(a))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    results = []
    
    for _ in range(t):
        _n = input_data[ptr] 
        a = input_data[ptr + 1]
        results.append(solve(a))
        ptr += 2
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
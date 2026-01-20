# Author: AlifSrSE

import sys

def solve(x, y, k):
    n = len(x)
    for i in range(n):
        reachable_all = True
        for j in range(n):
            if abs(x[i] - x[j]) + abs(y[i] - y[j]) > k:
                reachable_all = False
                break
        
        if reachable_all:
            return 1
            
    return -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr + 1])
        ptr += 2
        
        x = []
        y = []
        for _ in range(n):
            x.append(int(input_data[ptr]))
            y.append(int(input_data[ptr + 1]))
            ptr += 2
            
        results.append(str(solve(x, y, k)))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
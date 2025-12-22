#Author: AlifSrSE

import sys

def query(beginIndex, endIndex):
    print(f"? {beginIndex + 1} {endIndex + 1}")
    sys.stdout.flush()
    line = sys.stdin.readline()
    return int(line.strip())

def main():
    line = sys.stdin.readline()
    if not line:
        return
    N = int(line.strip())
    
    twoSums = [0] * (N - 1)
    for i in range(N - 1):
        twoSums[i] = query(i, i + 1)
        
    threeSum = query(0, 2)
    
    result = [0] * N
    result[0] = threeSum - twoSums[1]
    for i in range(1, N):
        result[i] = twoSums[i - 1] - result[i - 1]
        
    print(f"! {' '.join(map(str, result))}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
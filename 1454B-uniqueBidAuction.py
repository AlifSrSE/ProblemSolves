# Author: AlifSrSE
from collections import Counter
import sys

def solve(a):
    counts = Counter(a)
    uniques = [val for val in counts if counts[val] == 1]
    
    if not uniques:
        return -1
    
    min_unique = min(uniques)
    return a.index(min_unique) + 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        a = list(map(int, input_data[ptr+1 : ptr+1+n]))
        results.append(str(solve(a)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")
# Author: AlifSrSE
import sys

def solve(a):
    n = len(a)
    value_to_indices = {}
    for i, val in enumerate(a):
        if val not in value_to_indices:
            value_to_indices[val] = []
        value_to_indices[val].append(i)
    
    min_segments = float('inf')
    for val in value_to_indices:
        indices = value_to_indices[val]
        count = 0 if indices[0] == 0 else 1

        for i in range(len(indices) - 1):
            if indices[i] + 1 != indices[i+1]:
                count += 1
        if indices[-1] != n - 1:
            count += 1
        
        min_segments = min(min_segments, count)
    return min_segments

    
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys, math
from collections import defaultdict

input_data = sys.stdin.read().split()
iterator = iter(input_data)
test_cases = int(next(iterator))
results = []

for _ in range(test_cases):
    size = int(next(iterator))
    array_a = [int(next(iterator)) for _ in range(size)]
    array_b = [int(next(iterator)) for _ in range(size)]
    
    pairs = defaultdict(list)
    for idx in range(size):
        pairs[(array_a[idx], array_b[idx])].append(idx)
    
    is_valid = True
    unpaired = None
    swap_pairs = []
    
    for (val1, val2) in list(pairs.keys()):
        if val1 != val2 and (val1, val2) in pairs and (val2, val1) in pairs and val1 < val2:
            if len(pairs[(val1, val2)]) != len(pairs[(val2, val1)]):
                is_valid = False
                break
            count = len(pairs[(val1, val2)])
            for k in range(count):
                swap_pairs.append((pairs[(val1, val2)][k], pairs[(val2, val1)][k]))
    
    if not is_valid:
        results.append("-1")
        continue
    
    for (val1, val2) in list(pairs.keys()):
        if val1 == val2:
            indices = pairs[(val1, val2)]
            total = len(indices)
            half = total // 2
            for k in range(half):
                swap_pairs.append((indices[k], indices[k + half]))
            if total % 2 == 1:
                if unpaired is None:
                    unpaired = indices[-1]
                else:
                    is_valid = False
                    break
    
    if not is_valid:
        results.append("-1")
        continue
    
    total_positions = 2 * len(swap_pairs) + (1 if unpaired is not None else 0)
    if total_positions != size:
        results.append("-1")
        continue
    
    swap_pairs.sort(key=lambda pair: pair[0])
    left = [pair[0] for pair in swap_pairs]
    right = [pair[1] for pair in swap_pairs]
    right.reverse()
    target = left + ([unpaired] if unpaired is not None else []) + right
    
    current = list(range(size))
    positions = [0] * size
    for idx in range(size):
        positions[current[idx]] = idx
    
    operations = []
    for idx in range(size):
        if current[idx] == target[idx]:
            continue
        swap_pos = positions[target[idx]]
        current[idx], current[swap_pos] = current[swap_pos], current[idx]
        positions[current[idx]] = idx
        positions[current[swap_pos]] = swap_pos
        operations.append((idx, swap_pos))
    
    if len(operations) > size:
        results.append("-1")
    else:
        results.append(str(len(operations)))
        for idx1, idx2 in operations:
            results.append(f"{idx1 + 1} {idx2 + 1}")

sys.stdout.write("\n".join(results))
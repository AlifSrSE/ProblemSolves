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
        W = int(input_data[ptr + 1])
        ptr += 2
        w = [int(i) for i in input_data[ptr:ptr + n]]
        ptr += n
        
        limit = (W + 1) // 2
        single_index = -1
        for i in range(n):
            if limit <= w[i] <= W:
                single_index = i + 1
                break
        
        if single_index != -1:
            results.append(f"1\n{single_index}")
            continue
        
        candidates = []
        current_sum = 0
        for i in range(n):
            if w[i] < limit:
                candidates.append(i + 1)
                current_sum += w[i]
                if current_sum >= limit:
                    break
        
        if limit <= current_sum <= W:
            results.append(f"{len(candidates)}\n{' '.join(map(str, candidates))}")
        else:
            results.append("-1")
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
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
        m = int(input_data[ptr + 1])
        ptr += 2
        
        has_zero = False
        negative_count = 0
        min_abs = float('inf')
        abs_sum = 0
        
        for _ in range(n * m):
            val = int(input_data[ptr])
            ptr += 1
            if val == 0:
                has_zero = True
            elif val < 0:
                negative_count += 1
            
            a_val = abs(val)
            if a_val < min_abs:
                min_abs = a_val
            abs_sum += a_val
        
        res = abs_sum - (0 if (has_zero or negative_count % 2 == 0) else min_abs * 2)
        results.append(str(res))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
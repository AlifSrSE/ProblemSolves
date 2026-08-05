# Author: AlifSrSE
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    output = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        w = [int(x) for x in input_data[ptr : ptr + n]]
        ptr += n
        
        degrees = [0] * n
        for _ in range(n - 1):
            u = int(input_data[ptr]) - 1
            v = int(input_data[ptr + 1]) - 1
            ptr += 2
            degrees[u] += 1
            degrees[v] += 1
            
        # Collect weights multiplied by (degree - 1)
        sorted_weights = []
        for i in range(n):
            for _ in range(degrees[i] - 1):
                sorted_weights.append(w[i])
                
        sorted_weights.sort(reverse=True)
        
        current_sum = sum(w)
        result = [current_sum]
        
        for weight in sorted_weights:
            current_sum += weight
            result.append(current_sum)
            
        output.append(" ".join(map(str, result)))
        
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()
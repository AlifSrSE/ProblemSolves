# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def process_input():
    import sys
    input_data = sys.stdin.read().strip().split()
    if len(input_data) == 0:
        return
    
    num_tests = int(input_data[0])
    data_idx = 1
    results = []
    
    for _ in range(num_tests):
        length = int(input_data[data_idx])
        divisor = int(input_data[data_idx + 1])
        multiplier = int(input_data[data_idx + 2])
        data_idx = data_idx + 3
        
        threshold1 = length // (divisor + 1)
        threshold2 = length - divisor * multiplier
        min_threshold = min(threshold1, threshold2)
        
        output = [min_threshold for _ in range(length)]
        
        for iteration in range(min_threshold):
            left = iteration
            right = length - min_threshold + iteration
            difference = right - left
            increment = difference // divisor if divisor != 0 else 0
            
            for step in range(divisor + 1):
                position = left + step * increment
                if position > right:
                    position = right
                output[position] = iteration
        
        results.append(" ".join(str(x) for x in output))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    process_input()
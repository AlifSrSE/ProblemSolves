import sys
import io

def alif():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    t = int(input_data[0])
    pointer = 1
    
    output = []
    
    for _ in range(t):
        x = int(input_data[pointer])
        y = int(input_data[pointer + 1])
        z = int(input_data[pointer + 2])
        pointer += 3
        
        if x == y and x >= z:
            output.append("YES")
            output.append(f"{x} {z} {z}")
        elif x == z and z >= y:
            output.append("YES")
            output.append(f"{x} {y} {y}")
        elif y == z and y >= x:
            output.append("YES")
            output.append(f"{y} {x} {x}")
        else:
            output.append("NO")
            
    sys.stdout.write('\n'.join(output) + '\n')

alif()
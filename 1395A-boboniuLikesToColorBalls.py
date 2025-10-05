import sys

def alif():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    data_idx = 0
    t = int(input_data[data_idx])
    data_idx += 1
    output = []
    
    for _ in range(t):
        r = int(input_data[data_idx])
        g = int(input_data[data_idx + 1])
        b = int(input_data[data_idx + 2])
        w = int(input_data[data_idx + 3])
        data_idx += 4
        
        def count_odd(r, g, b, w):
            return r % 2 + g % 2 + b % 2 + w % 2

        if count_odd(r, g, b, w) <= 1:
            output.append("Yes")
        
        elif r > 0 and g > 0 and b > 0:
            r_new = r - 1
            g_new = g - 1
            b_new = b - 1
            w_new = w + 1
            
            if count_odd(r_new, g_new, b_new, w_new) <= 1:
                output.append("Yes")
            else:
                output.append("No")
        else:
            output.append("No")

    sys.stdout.write('\n'.join(output) + '\n')

alif()

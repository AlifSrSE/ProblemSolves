import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return

    data_idx = 0
    t = int(data[data_idx])
    data_idx += 1
    output_lines = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        s = data[data_idx]
        data_idx += 1
        num = 0
        z = []
        a = []
        v = [0] * n
        
        for p in range(n):
            current_char = s[p]
            cur = 0
            if current_char == '0':
                if a:
                    cur = a.pop()
                else:
                    num += 1
                    cur = num
                z.append(cur)
            elif current_char == '1':
                if z:
                    cur = z.pop()
                else:
                    num += 1
                    cur = num
                a.append(cur)
            v[p] = cur

        output_lines.append(str(num))
        output_lines.append(' '.join(map(str, v)))
        
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
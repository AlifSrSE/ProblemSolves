import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    
    data_idx = 0
    t = int(data[data_idx])
    data_idx += 1
    output = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        a = [int(x) for x in data[data_idx : data_idx + n]]
        data_idx += n
        idx = -1
        
        for p in range(1, n - 1):
            if a[n - 1] >= a[0] + a[p]:
                idx = p + 1
                break

        if idx > 0:
            output.append(f"1 {idx} {n}")
        else:
            output.append("-1")
            
    sys.stdout.write('\n'.join(output) + '\n')

alif()

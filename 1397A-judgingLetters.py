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
        strings = data[data_idx : data_idx + n]
        data_idx += n
        v = [0] * 26
        
        for s in strings:
            for char in s:
                v[ord(char) - ord('a')] += 1
        res = True

        for count in v:
            if count % n != 0:
                res = False
                break
        
        if res:
            output.append("YES")
        else:
            output.append("NO")
            
    sys.stdout.write('\n'.join(output) + '\n')

alif()

import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    strings = data[1:]
    output = []
    
    for s in strings:
        v = []
        cnt = 0
        
        for char in s:
            if char == '1':
                cnt += 1
            else:
                if cnt > 0:
                    v.append(cnt)
                cnt = 0
        
        if cnt > 0:
            v.append(cnt)
        v.sort(reverse=True)
        total = 0
        
        for p in range(0, len(v), 2):
            total += v[p]
            
        output.append(str(total))
            
    sys.stdout.write('\n'.join(output) + '\n')

alif()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def check(a, length, time):
    
    x = 0.0
    rem = time
    
    for p in range(1, len(a)):
        dist = a[p] - a[p - 1]
        speed = float(p)
        
        if dist < speed * rem:
            x += dist
            rem -= dist / speed
        else:
            x += speed * rem
            rem = 0.0
            break
    
    y = 0.0
    rem = time
    
    for p in range(len(a) - 2, -1, -1):
        dist = a[p + 1] - a[p]
        speed = float(len(a) - 1 - p)
        
        if dist < speed * rem:
            y += dist
            rem -= dist / speed
        else:
            y += speed * rem
            rem = 0.0
            break
            
    return x + y <= length

def alif():
    data = sys.stdin.read().split()
    if not data:
        return

    data_idx = 0
    t = int(data[data_idx])
    data_idx += 1
    
    output_lines = []
    
    for _ in range(t):
        n_float = float(data[data_idx])
        data_idx += 1
        length = float(data[data_idx])
        data_idx += 1
        
        n_int = int(n_float)
        
        a = [0.0] * (n_int + 2)
        
        for p in range(1, n_int + 1):
            a[p] = float(data[data_idx])
            data_idx += 1
        
        a[n_int + 1] = length

        left = 0.0
        right = 1e10
        eps = 1e-7
        res = 0.0
        
        while right - left > eps:
            mid = (left + right) / 2.0
            if check(a, length, mid):
                res = mid
                left = mid
            else:
                right = mid

        output_lines.append(f"{res:.8f}")

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()

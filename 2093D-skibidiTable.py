# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def get_number(x, y, n):
    x -= 1
    y -= 1
    size = 1 << n 
    
    def solve(x, y, size, base):
        if size == 2:
            if x == 0 and y == 0: return base + 1
            if x == 1 and y == 1: return base + 2
            if x == 1 and y == 0: return base + 3
            if x == 0 and y == 1: return base + 4
        
        half = size // 2
        if x < half and y < half:
            return solve(x, y, half, base)
        elif x >= half and y >= half:
            return solve(x - half, y - half, half, base + half * half)
        elif x >= half:
            return solve(x - half, y, half, base + 2 * half * half)
        else:
            return solve(x, y - half, half, base + 3 * half * half)
    
    return solve(x, y, size, 0)

def get_position(d, n):
    size = 1 << n
    
    def solve(d, size, base_x, base_y, base_num):
        if size == 2:
            if d == base_num + 1: return (base_x + 1, base_y + 1)
            if d == base_num + 2: return (base_x + 2, base_y + 2)
            if d == base_num + 3: return (base_x + 2, base_y + 1)
            if d == base_num + 4: return (base_x + 1, base_y + 2)
        
        half = size // 2
        quad_size = half * half
        
        if d <= base_num + quad_size:
            return solve(d, half, base_x, base_y, base_num)
        elif d <= base_num + 2 * quad_size:  
            return solve(d, half, base_x + half, base_y + half, base_num + quad_size)
        elif d <= base_num + 3 * quad_size:  
            return solve(d, half, base_x + half, base_y, base_num + 2 * quad_size)
        else: 
            return solve(d, half, base_x, base_y + half, base_num + 3 * quad_size)
    
    return solve(d, size, 0, 0, 0)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    
    for _ in range(q):
        query = input().split()
        if query[0] == '->':
            x, y = map(int, query[1:])
            print(get_number(x, y, n))
        else:
            d = int(query[1])
            x, y = get_position(d, n)
            print(x, y)
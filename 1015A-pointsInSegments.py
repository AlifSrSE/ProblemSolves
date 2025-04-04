# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    
    points = [x for x in range(1, m + 1) 
             if all(not (x >= l[i] and x <= r[i]) for i in range(n))]
    
    return points

result = solve()
print(len(result))
print(' '.join(map(str, result)))
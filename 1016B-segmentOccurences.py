# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    q = int(input())
    s = input()
    t = input()
    
    l = []
    r = []
    for _ in range(q):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    
    begin_indices = [i for i in range(len(s)) if s.startswith(t, i)]
    
    result = []
    for i in range(q):
        count = sum(1 for begin in begin_indices 
                   if begin >= l[i] - 1 and begin + len(t) <= r[i])
        result.append(str(count))
    
    return '\n'.join(result)

print(solve())
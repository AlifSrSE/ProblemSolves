# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input()) 
    a = input()
    b = input()
    
    group_count = {}
    for i in range(len(a)):
        group = a[i] + b[i]
        group_count[group] = group_count.get(group, 0) + 1
    
    result = (group_count.get('00', 0) * group_count.get('10', 0) +
              group_count.get('00', 0) * group_count.get('11', 0) +
              group_count.get('01', 0) * group_count.get('10', 0))
    
    return result

print(solve())
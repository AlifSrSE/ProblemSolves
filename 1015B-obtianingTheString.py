# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    s = list(input())
    t = input()
    
    indices = []
    
    for i in range(len(t)):
        try:
            index = s.index(t[i], i)
        except ValueError:
            return "-1"
            
        for j in range(index - 1, i - 1, -1):
            s[j], s[j + 1] = s[j + 1], s[j]
            indices.append(j + 1) 
            
    return f"{len(indices)}\n{' '.join(map(str, indices))}"

print(solve())
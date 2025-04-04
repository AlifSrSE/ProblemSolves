# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    k = int(input())
    s = input()
    
    result = []
    skip_count = (len(s) - k) // 2
    depth = 0
    
    for ch in s:
        if ch == '(':
            if skip_count > 0:
                skip_count -= 1
            else:
                result.append(ch)
                depth += 1
        elif ch == ')' and depth > 0:
            result.append(ch)
            depth -= 1
    
    return ''.join(result)

print(solve())
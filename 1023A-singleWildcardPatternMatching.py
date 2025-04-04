# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    s = input()
    t = input()
    
    wildcard_index = s.find('*')
    
    if wildcard_index == -1:
        return s == t
    else:
        return (len(s) - 1 <= len(t) and 
                t.startswith(s[:wildcard_index]) and 
                t.endswith(s[wildcard_index + 1:]))

print("YES" if solve() else "NO")
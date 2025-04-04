# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    s = input()
    
    color_count = {}
    for color in s:
        color_count[color] = color_count.get(color, 0) + 1
    
    return len(s) == 1 or any(count != 1 for count in color_count.values())

print("Yes" if solve() else "No")
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1167/problem/B

def alif(k):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    
    for row in range(len(VOWELS), k + 1):
        if row * row > k:
            break
        if k % row == 0:
            col = k // row
            grid = [[VOWELS[(r + c) % len(VOWELS)] for c in range(col)] for r in range(row)]
            return ''.join(''.join(row) for row in grid)
    
    return "-1"

k = int(input())
print(alif(k))
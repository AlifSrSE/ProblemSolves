# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1155/problem/B

def alif(s):
    round = (len(s) - 11) // 2
    erased = [False] * len(s)
    
    index = 0
    for i in range(round):
        while index < len(erased) and s[index] == '8':
            index += 1
        
        if index == len(erased):
            return True
        
        erased[index] = True
        index += 1
    
    index = 0
    for i in range(round):
        while index < len(erased) and (erased[index] or s[index] != '8'):
            index += 1
        
        if index == len(erased):
            return False
        
        erased[index] = True
        index += 1
    
    for i in range(len(s)):
        if not erased[i]:
            return s[i] == '8'

n = int(input())
s = input()
print("YES" if alif(s) else "NO")
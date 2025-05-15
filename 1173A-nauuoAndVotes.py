# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1173/problem/A

def alif(s):
    begin_index = s.find('8')
    return begin_index >= 0 and len(s) - begin_index >= 11

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print("YES" if alif(s) else "NO")
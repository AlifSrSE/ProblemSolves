# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
 
def solve():
    s = input()
    b = 0
    cnt = 0
    for c in s:
        if c == '0':
            cnt += 1
        else:
            b = max(b, cnt + 1)
    print(len(s) - b)
 
t = int(input())
for _ in range(t):
    solve()
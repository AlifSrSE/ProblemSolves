# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    s = input()
    t = input()
    pref = 0
    i = 0
    while i < len(s) and i < len(t):
        if s[i] == t[i]:
            pref += 1
        else:
            break
        i += 1

    if pref:
        print(pref + 1 + (len(s) - pref) + (len(t) - pref))
    else:
        print(len(s) + len(t))

q = int(input())
for _ in range(q):
    solve()
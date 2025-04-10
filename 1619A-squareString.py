# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

t = int(input())
for _ in range(t):
    s = input().strip()
    if len(s) % 2 != 0:
        print("NO")
        continue
    h = len(s) // 2
    sq = True
    for p in range(h):
        if s[p] != s[h + p]:
            sq = False
            break
    print("YES" if sq else "NO")
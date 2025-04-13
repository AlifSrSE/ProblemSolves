# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

t = input().strip()
n = len(t)
found = False
s_candidate = ""

for k in range(1, n // 2 + 1):
    if t[:k] == t[-k:]:
        s = t[:-k]
        if len(s) > 0 and k < len(s):
            found = True
            s_candidate = s
            break

if found:
    print("YES")
    print(s_candidate)
else:
    print("NO")
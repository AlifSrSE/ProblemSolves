# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
ans = []
res_strings = [None] * n

for i in range(n-1, -1, -1):
    c = s[i]

    if ans and ans[-1] == c:
        ans.pop()
    else:
        ans.append(c)
    cur = ''.join(reversed(ans))

    if len(cur) > 10:
        cur_fmt = cur[:5] + "..." + cur[-2:]
    else:
        cur_fmt = cur
    res_strings[i] = f"{len(cur)} {cur_fmt}"

print("\n".join(res_strings))

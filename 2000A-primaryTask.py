# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    s = str(a)
    return len(s) >= 3 and s.startswith("10") and s[2] != '0' and int(s[2:]) >= 2

t = int(input())
for _ in range(t):
    a = int(input())
    print("YES" if solve(a) else "NO")

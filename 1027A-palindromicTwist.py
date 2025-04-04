# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    i, j = 0, len(s) - 1
    while i < j:
        distance = abs(ord(s[i]) - ord(s[j]))
        if distance != 0 and distance != 2:
            return False
        i += 1
        j -= 1
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    print("YES" if solve(s) else "NO")
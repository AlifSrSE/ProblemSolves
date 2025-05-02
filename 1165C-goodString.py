# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1165/problem/C

def alif(s):
    deleted = []
    index = 0
    while index + 1 < len(s):
        ch = s[index]
        ch1 = s[index + 1]

        if ch != ch1:
            deleted.extend([ch, ch1])
            index += 2
        elif index + 2 < len(s) and ch != s[index + 2]:
            deleted.extend([ch, s[index + 2]])
            index += 3
        else:
            index += 2
    
    return f"{len(s) - len(deleted)}\n{''.join(deleted)}"

n = int(input())
s = input()
print(alif(s))
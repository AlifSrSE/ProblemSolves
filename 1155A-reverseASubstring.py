# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1155/problem/A

def alif(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return f"YES\n{i + 1} {i + 2}"
    return "NO"

n = int(input())
s = input()
print(alif(s))
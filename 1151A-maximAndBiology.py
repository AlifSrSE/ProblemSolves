# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1151/problem/A

def alif(s):
    GENOME = "ACTG"
    min_diff = float('inf')

    for i in range(len(s) - len(GENOME) + 1):
        total_diff = 0
        for j in range(len(GENOME)):
            diff = abs(ord(s[i + j]) - ord(GENOME[j]))
            total_diff += min(diff, 26 - diff)
        min_diff = min(min_diff, total_diff)

    return min_diff

# Input handling
_ = int(input())
s = input()
print(alif(s))

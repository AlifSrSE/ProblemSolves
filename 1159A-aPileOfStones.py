# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1159/problem/A

def alif(s):
    min_val = 0
    value = 0
    for char in s:
        if char == '+':
            value += 1
        else:
            value -= 1
        min_val = min(min_val, value)
    return value - min_val

if __name__ == "__main__":
    input()
    s = input()
    print(alif(s))
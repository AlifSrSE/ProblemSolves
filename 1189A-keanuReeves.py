# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1189/problem/A

def alif():
    n = int(input())
    s = input()
    cnt = 0
    for char in s:
        if char == '0':
            cnt += 1
        elif char == '1':
            cnt -= 1
    
    if cnt != 0:
        print(1)
        print(s)
    else:
        print(2)
        print(s[0], s[1:])

if __name__ == "__main__":
    alif()

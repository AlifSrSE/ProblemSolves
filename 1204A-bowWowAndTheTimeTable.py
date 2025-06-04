# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1204/problem/A

def alif():
    s = input()
    z = False

    if s == "0":
        z = True
    elif s.startswith('1'):
        z = True

        for p in range(1, len(s)):
            if s[p] != '0':
                z = False
                break
    cnt = (len(s) + 1 - (1 if z else 0)) // 2
    
    print(cnt)

if __name__ == "__main__":
    alif()
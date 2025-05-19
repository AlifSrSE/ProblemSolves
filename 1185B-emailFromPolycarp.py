# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1185/problem/B

def alif():
    n = int(input())
    for _ in range(n):
        s = input()
        t = input()
        idx = 0
        possible = True
        for p in range(len(t)):
            if idx < len(s) and s[idx] == t[p]:
                idx += 1
            elif p > 0 and t[p] == t[p - 1]:
                pass
            else:
                possible = False
                break
        if idx < len(s):
            possible = False
        print("YES" if possible else "NO")

if __name__ == "__main__":
    alif()

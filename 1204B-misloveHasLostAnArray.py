# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1204/problem/B

def alif():
    n, l, r = map(int, input().split())
    fl = (n - l + 1)

    for p in range(l):
        if p >= 1:
            fl += (1 << p)
    r -= 1
    fr = 0

    for p in range(n):
        power_val = p if p < r else r
        fr += (1 << power_val)
    
    print(fl, fr)

if __name__ == "__main__":
    alif()
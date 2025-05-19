# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1185/problem/A

def alif():
    x = list(map(int, input().split()))
    d = x.pop()
    x.sort()
    t1 = x[0] - x[1] + d
    t2 = x[1] + d - x[2]
    t = (t1 if t1 > 0 else 0) + (t2 if t2 > 0 else 0)
    print(t)

if __name__ == "__main__":
    alif()
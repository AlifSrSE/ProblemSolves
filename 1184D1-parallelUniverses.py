# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1184/problem/D1

def alif():
    length, pos, m, t = map(int, input().split())
    for _ in range(t):
        action, w = map(int, input().split())
        if action == 0:
            length -= w if w < pos else length - w
            pos -= w if w < pos else 0
        else:
            length += 1
            pos += 1 if w <= pos else 0
        print(length, pos)

if __name__ == "__main__":
    alif()
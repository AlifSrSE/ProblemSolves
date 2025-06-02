# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1200/problem/A

def alif():
    cap = 10
    n = int(input())
    s = input()
    a = [0] * cap

    for p in range(n):
        if s[p] == 'L':
            for u in range(cap):
                if a[u] == 0:
                    a[u] = 1
                    break
        elif s[p] == 'R':
            for u in range(cap - 1, -1, -1):
                if a[u] == 0:
                    a[u] = 1
                    break
        else:
            a[int(s[p])] = 0

    for p in range(cap):
        print(a[p], end='')
    print()

if __name__ == "__main__":
    alif()
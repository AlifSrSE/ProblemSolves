# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1196/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        print((x + y + z) // 2)

if __name__ == "__main__":
    alif()
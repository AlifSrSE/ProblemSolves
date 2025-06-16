# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1217/problem/A

def alif():
    t = int(input())
    while t > 0:
        a, b, n = map(int, input().split())
        tmp = a + n - b - 1

        if tmp < 0:
            print(0)
        else:
            result = 1 + min(tmp // 2, n)
            print(result)
        t -= 1

if __name__ == "__main__":
    alif()
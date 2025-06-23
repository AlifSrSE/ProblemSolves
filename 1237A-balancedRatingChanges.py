# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1237/problem/A

def alif():
    n = int(input())
    diff = 0 

    for _ in range(n):
        x = int(input())
        if x % 2 != 0:
            if diff >= 0:
                x -= 1
                diff -= 1
            else:
                x += 1
                diff += 1
        print(x // 2)

if __name__ == "__main__":
    alif()
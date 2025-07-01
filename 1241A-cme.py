# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1241/problem/A

def alif():
    q = int(input())

    for _ in range(q):
        n = int(input())

        if n <= 4:
            print(4 - n)
        else:
            if n % 2 != 0:
                print(1)
            else:
                print(0)

if __name__ == "__main__":
    alif()
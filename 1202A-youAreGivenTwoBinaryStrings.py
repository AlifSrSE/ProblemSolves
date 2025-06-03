# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1202/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        x_str = input()
        y_str = input()

        a = 0
        while a < len(y_str) and y_str[len(y_str) - 1 - a] == '0':
            a += 1

        b = 0
        while b < len(x_str) - a and x_str[len(x_str) - 1 - a - b] == '0':
            b += 1
        print(b)

if __name__ == "__main__":
    alif()
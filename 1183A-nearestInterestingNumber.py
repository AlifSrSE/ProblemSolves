# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1183/problem/A

def alif(a):
    i = a
    while True:
        if sum(int(digit) for digit in str(i)) % 4 == 0:
            return i
        i += 1

if __name__ == "__main__":
    a = int(input())
    print(alif(a))

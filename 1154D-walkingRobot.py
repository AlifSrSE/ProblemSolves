# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1154/problem/D

def alif(s, b, a):
    charge_b = b
    charge_a = a

    for i in range(len(s)):
        if charge_b == 0 and charge_a == 0:
            return i

        if s[i] == 0:
            if charge_a != 0:
                charge_a -= 1
            else:
                charge_b -= 1
        else:
            if charge_b != 0 and charge_a != a:
                charge_b -= 1
                charge_a += 1
            else:
                charge_a -= 1

    return len(s)

if __name__ == "__main__":
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    print(alif(s, b, a))

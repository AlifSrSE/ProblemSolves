# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1194/problem/D

def alif():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if k % 3 != 0:
            print("Alice" if n % 3 != 0 else "Bob")
        else:
            m = n % (k + 1)
            print("Alice" if (m % 3 != 0 or m == k) else "Bob")

if __name__ == "__main__":
    alif()
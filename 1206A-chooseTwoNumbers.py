# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1206/problem/A

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    max_a = max(a)
    max_b = max(b)
    print(max_a, max_b)

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1183/problem/B

def alif(a, k):
    min_price = min(a)
    max_price = max(a)
    return -1 if min_price + k < max_price - k else min_price + k

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(alif(a, k))

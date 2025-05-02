# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1175/problem/A

def alif(n, k):
    result = 0
    while n != 0:
        if n % k == 0:
            result += 1
            n //= k
        else:
            result += n % k
            n -= n % k
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(alif(n, k))
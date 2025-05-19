# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1185/problem/C1

def alif():
    """
    Solves Codeforces Problem 1185C1: Exam in BerSU (Easy Version).
    """
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    B = 101
    h = [0] * B

    s = 0
    for p in range(n):
        t = a[p]
        cur = s
        rem = 0
        for u in range(B - 1, 0, -1):
            if cur + t > m:
                diff = cur + t - m
                if diff > u * h[u]:
                    rem += h[u]
                    cur -= u * h[u]
                else:
                    x = (diff + u - 1) // u
                    rem += x
                    cur -= x * u
                    break
        print(rem, end=" ")
        h[t] += 1
        s += t
    print()

if __name__ == "__main__":
    alif()

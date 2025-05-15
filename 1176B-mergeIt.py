# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1176/problem/B

def alif(a):
    counts = [0] * 3
    for ai in a:
        counts[ai % 3] += 1

    min12 = min(counts[1], counts[2])
    return counts[0] + min12 + (counts[1] - min12) // 3 + (counts[2] - min12) // 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(alif(a))

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1187/problem/B

def alif():
    N_ALPHA = 26
    v = [[] for _ in range(N_ALPHA)]

    n = int(input())
    s = input()
    for p in range(len(s)):
        v[ord(s[p]) - ord('a')].append(p + 1)

    m = int(input())
    for _ in range(m):
        t = input()
        w = [0] * N_ALPHA
        for p in range(len(t)):
            w[ord(t[p]) - ord('a')] += 1

        ans = 0
        for p in range(N_ALPHA):
            if w[p] == 0:
                continue
            ans = max(ans, v[p][w[p] - 1])
        print(ans)

if __name__ == "__main__":
    alif()

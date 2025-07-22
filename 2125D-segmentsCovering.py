# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2125/problem/D

MOD = 998244353

def modexp(ai, ei):
    result = 1
    while ei:
        if ei & 1:
            result = result * ai % MOD
        ai = ai * ai % MOD
        ei >>= 1
    return result

def alif():
    ni, mi = map(int, input().split())
    by_ri = [[] for _ in range(mi + 1)]
    BI = 1

    for _ in range(ni):
        li, ri, pi, qi = map(int, input().split())
        inv_qi = modexp(qi, MOD - 2)
        qpi = (qi - pi) % MOD
        BI = BI * qpi % MOD * inv_qi % MOD
        inv_qpi = modexp(qpi, MOD - 2)
        wi = pi % MOD * inv_qpi % MOD
        by_ri[ri].append((li, wi))

    dpi = [0] * (mi + 1)
    dpi[0] = 1

    for xi in range(1, mi + 1):
        curi = 0
        for li, wi in by_ri[xi]:
            curi = (curi + dpi[li - 1] * wi) % MOD
        dpi[xi] = curi

    ans = dpi[mi] * BI % MOD
    print(ans)

if __name__ == "__main__":
    alif()
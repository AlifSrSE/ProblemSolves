# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2112/problem/E

def alif():
    ti = int(input())
    qsi = list(map(int, input().split()))
    MI = max(qsi, default=1)
    sipf = [0] * (MI + 1)
    primes = []

    for i in range(2, MI + 1):
        if sipf[i] == 0:
            sipf[i] = i
            primes.append(i)
        for p in primes:
            vi = p * i
            if p > sipf[i] or vi > MI:
                break
            sipf[vi] = p

    INF = 10**9
    hi = [INF] * (MI + 1)
    hi[1] = 0

    def gen(idx, val, ifac, idivs):
        if idx == len(ifac):
            idivs.append(val)
            return
        pi, ci = ifac[idx]
        vi = val
        for e in range(ci + 1):
            gen(idx + 1, vi, ifac, idivs)
            vi *= pi

    for xi in range(2, MI + 1):
        ifac = []
        yi = xi
        while yi > 1:
            pi = sipf[yi]
            cnt = 0
            while yi % pi == 0:
                yi //= pi
                cnt += 1
            ifac.append((pi, cnt))
        idivs = []
        gen(0, 1, ifac, idivs)
        best = INF

        for di in idivs:
            if di >= 3:
                s1 = di - 2
                other = xi // di
                cand = hi[s1] + hi[other] + 1
                best = min(best, cand)
        hi[xi] = best

    for m in qsi:
        if m == 1:
            print(1)
        elif hi[m] >= INF:
            print(-1)
        else:
            print(hi[m] + 1)

if __name__ == "__main__":
    alif()
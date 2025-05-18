# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1184/problem/B1

def alif():
    si, bi = map(int, input().split())
    ai = []
    ai_vals = list(map(int, input().split()))
    for p in range(si):
        ai.append((ai_vals[p], p))

    d = []
    for _ in range(bi):
        di, ki = map(int, input().split())
        d.append((di, ki))

    ai.sort()
    d.sort()

    sg = [0] * bi
    if bi > 0:
        sg[0] = d[0][1]
        for p in range(1, bi):
            sg[p] = sg[p - 1] + d[p][1]

    res = [0] * si
    ind = 0
    for p in range(si):
        while ind < bi and ai[p][0] >= d[ind][0]:
            ind += 1
        gold = sg[ind - 1] if ind > 0 else 0
        res[ai[p][1]] = gold

    print(*res)

if __name__ == "__main__":
    alif()
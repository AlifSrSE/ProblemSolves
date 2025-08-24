# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

MOD = 998244353

def build_next_greater(a):
    n = len(a)
    nge = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        nge[i] = st[-1] if st else -1
        st.append(i)
    return nge

def build_next_smaller(a):
    n = len(a)
    nse = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while st and a[st[-1]] >= a[i]:
            st.pop()
        nse[i] = st[-1] if st else -1
        st.append(i)
    return nse

def build_next_neq(a):
    n = len(a)
    nneq = [-1]*n
    for i in range(n-2, -1, -1):
        if a[i+1] != a[i]:
            nneq[i] = i+1
        else:
            nneq[i] = nneq[i+1]
    nneq[-1] = -1
    return nneq

def alif():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    nge = build_next_greater(a)
    nse = build_next_smaller(a)
    nneq = build_next_neq(a)
    upEnd = [0]*n
    dnEnd = [0]*n

    for i in range(n-1, -1, -1):
        upEnd[i] = upEnd[nge[i]] if nge[i] != -1 else i
        dnEnd[i] = dnEnd[nse[i]] if nse[i] != -1 else i

    INF = 10**18
    end3 = [INF]*n
    end4 = [INF]*n
    seq3 = [None]*n
    seq4 = [None]*n

    for s in range(n):
        j = nneq[s]
        if j == -1:
            continue
        if a[j] > a[s]:
            p1 = upEnd[j]
            opp_start = nse[p1]

            if opp_start == -1:
                continue
            p2 = dnEnd[opp_start]
            end3[s] = p2
            seq3[s] = (s, p1, p2)
            opp_start2 = nge[p2]

            if opp_start2 != -1:
                p3 = upEnd[opp_start2]
                end4[s] = p3
                seq4[s] = (s, p1, p2, p3)
        else:
            p1 = dnEnd[j]
            opp_start = nge[p1]
            if opp_start == -1:
                continue

            p2 = upEnd[opp_start]
            end3[s] = p2
            seq3[s] = (s, p1, p2)
            opp_start2 = nse[p2]
            if opp_start2 != -1:
                p3 = dnEnd[opp_start2]
                end4[s] = p3
                seq4[s] = (s, p1, p2, p3)

    best4End = [INF]*(n+1)
    best4Start = [-1]*(n+1)
    best3End = [INF]*(n+1)
    best3Start = [-1]*(n+1)
    best4End[n] = INF
    best3End[n] = INF

    for i in range(n-1, -1, -1):
        if end4[i] <= best4End[i+1]:
            best4End[i] = end4[i]
            best4Start[i] = i
        else:
            best4End[i] = best4End[i+1]
            best4Start[i] = best4Start[i+1]

        if end3[i] <= best3End[i+1]:
            best3End[i] = end3[i]
            best3Start[i] = i
        else:
            best3End[i] = best3End[i+1]
            best3Start[i] = best3Start[i+1]

    out = []
    for _ in range(q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1

        if best4End[L] <= R:
            s = best4Start[L]
            i1, i2, i3, i4 = seq4[s]
            out.append("4")
            out.append(f"{i1+1} {i2+1} {i3+1} {i4+1} ")
            continue

        if best3End[L] <= R:
            s = best3Start[L]
            i1, i2, i3 = seq3[s]
            out.append("3")
            out.append(f"{i1+1} {i2+1} {i3+1} ")
            continue

        out.append("0")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    alif()
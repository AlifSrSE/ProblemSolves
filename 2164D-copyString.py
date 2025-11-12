# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import bisect

input = sys.stdin.readline

def feasible(k, pos, t, n):
    out = [0] * (n + 1)
    lb = 1
    for i in range(1, n + 1):
        v = pos[ord(t[i - 1]) - ord('a')]
        need = max(lb, i - k)
        it = bisect.bisect_left(v, need)
        if it == len(v) or v[it] > i:
            return False, []
        out[i] = v[it]
        lb = out[i]
    return out[1] == 1, out


def alif():
    T = int(input())
    for _ in range(T):
        n, kmax = map(int, input().split())
        s = input().strip()
        t = input().strip()

        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i + 1)

        lo, hi = 0, n - 1
        ans = -1
        best = []

        while lo <= hi:
            mid = (lo + hi) // 2
            ok, tmp = feasible(mid, pos, t, n)
            if ok:
                ans = mid
                best = tmp
                hi = mid - 1
            else:
                lo = mid + 1

        if ans == -1 or ans > kmax:
            print(-1)
            continue

        print(ans)
        if ans == 0:
            continue

        cur = list(s)
        nxt = ['?'] * n
        for step in range(1, ans + 1):
            nxt[0] = cur[0]
            for i in range(2, n + 1):
                if step <= i - best[i]:
                    nxt[i - 1] = cur[i - 2]
                else:
                    nxt[i - 1] = cur[i - 1]
            print(''.join(nxt))
            cur, nxt = nxt, cur


if __name__ == "__main__":
    alif()

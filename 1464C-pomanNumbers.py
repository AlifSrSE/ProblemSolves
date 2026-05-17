# Author: AlifSrSE
import sys

def solve():
    input = sys.stdin.readline
    n, T = map(int, input().split())
    s = input().strip()
    first = 1 << (ord(s[0]) - ord('a'))
    cnt = [0] * 26
    total = 0

    for c in s[1:]:
        v = 1 << (ord(c) - ord('a'))
        total += v
        cnt[ord(c) - ord('a')] += 1
    target = T + first

    if (total + target) % 2:
        print("No")
        return
    need = (total + target) // 2

    if need < 0 or need > total:
        print("No")
        return

    for b in range(25, -1, -1):
        val = 1 << b
        take = min(cnt[b], need // val)
        need -= take * val

    print("Yes" if need == 0 else "No")

if __name__ == "__main__":
    solve()
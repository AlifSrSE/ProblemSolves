# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from bisect import bisect_left, insort

input = sys.stdin.readline

def alif():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        upgradable = []
        normal = []
        
        for i in range(m):
            if c[i] > 0:
                upgradable.append((b[i], c[i]))
            else:
                normal.append((b[i], c[i]))
        swords = sorted(a)
        upgradable.sort()
        kills = 0

        for life, new_sword in upgradable:
            idx = bisect_left(swords, life)
            if idx < len(swords):
                used_sword = swords.pop(idx)
                insort(swords, max(used_sword, new_sword))
                kills += 1

        remaining_swords = sorted(swords)
        normal.sort()
        i = j = 0

        while i < len(remaining_swords) and j < len(normal):
            if remaining_swords[i] >= normal[j][0]:
                kills += 1
                i += 1
                j += 1
            else:
                i += 1

        print(kills)

if __name__ == "__main__":
    alif()

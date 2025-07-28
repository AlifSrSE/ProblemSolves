# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1257/problem/D

import sys

def alif():
    t = int(sys.stdin.readline())
    while t:
        n, m_battles_count = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        bt = []
        for _ in range(m_battles_count):
            d, s = map(int, sys.stdin.readline().split())
            bt.append((d, s))
        
        bt.sort(key=lambda x: x[0], reverse=True)

        mxa = 0
        
        for val in a:
            mxa = max(mxa, val)
        
        if mxa > bt[0][0]:
            sys.stdout.write("-1\n")
            t -= 1
            continue
        
        b = []
        b.append(bt[0])
        for p in range(1, m_battles_count):
            if bt[p][1] <= b[-1][1]: 
                continue
            b.append(bt[p])
        
        idx = 0
        mx = 0
        cur = 0
        cnt = 0
        
        for p in range(n):
            mx = max(mx, a[p])
            
            if mx <= b[idx][0] and cur < b[idx][1]:
                cur += 1
            elif idx + 1 < len(b) and mx <= b[idx + 1][0]:
                idx += 1
                cur = 1
            else:
                idx = 0
                cur = 1
                cnt += 1
        
        sys.stdout.write(f"{cnt + 1}\n")
        t -= 1

if __name__ == "__main__":
    alif()
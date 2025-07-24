# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1253/problem/B

import sys

def alif():
    a = set()
    b = set()
    d = []
    n = int(sys.stdin.readline())
    events = list(map(int, sys.stdin.readline().split()))
    res = True
    cnt = 0

    for x in events:
        cnt += 1
        
        if x > 0:
            if x in b:
                res = False
                break
            a.add(x)
            b.add(x)
            
        else:
            person_id = -x
            if person_id not in a:
                res = False
                break
            a.remove(person_id)
            
            if len(a) == 0:
                d.append(cnt)
                cnt = 0
                b.clear()
                
    if cnt > 0:
        res = False

    if res:
        sys.stdout.write(f"{len(d)}\n")
        sys.stdout.write(" ".join(map(str, d)) + "\n")
    else:
        sys.stdout.write("-1\n")

if __name__ == "__main__":
    alif()
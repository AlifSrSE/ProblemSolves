# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, b, ta, fa, tb, fb):
    if ta == tb:
        return abs(fa - fb)
    else:
        if fa < a:
            transfer = a
        elif fa > b:
            transfer = b
        else:
            transfer = fa
        
        return abs(ta - tb) + abs(fa - transfer) + abs(fb - transfer)

n, h = map(int, input().split())
a, b, k = map(int, input().split())

for _ in range(k):
    ta, fa, tb, fb = map(int, input().split())
    print(solve(a, b, ta, fa, tb, fb))
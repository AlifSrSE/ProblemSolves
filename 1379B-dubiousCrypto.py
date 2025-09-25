# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    l, r, m = map(int, input().split())

    for a in range(l, r + 1):
        na = m // a
        
        if na > 0:
            diff1 = m - na * a
            if l - r <= diff1 <= r - l:
                if diff1 >= 0:
                    b = l + diff1
                    c = l
                else:
                    b = l
                    c = l - diff1
                print(a, b, c)
                return
        
        na2 = na + 1
        diff2 = m - na2 * a
        if l - r <= diff2 <= r - l:
            if diff2 >= 0:
                b = l + diff2
                c = l
            else:
                b = l
                c = l - diff2
            print(a, b, c)
            return

t = int(input())
for _ in range(t):
    alif()

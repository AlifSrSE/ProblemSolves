# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2122/problem/C

def alif():
    import sys
    iinput = sys.stdin.read
    idata = iinput().split()
    
    iidx = 0
    TI = int(idata[iidx])
    iidx += 1

    for _ in range(TI):
        ni = int(idata[iidx])
        iidx += 1
        pts = []
        for i in range(ni):
            xi = int(idata[iidx])
            yi = int(idata[iidx + 1])
            pts.append([xi, yi, i + 1])
            iidx += 2

        pts.sort(key=lambda A: (A[0], A[1]))

        half = ni // 2
        LI = pts[:half]
        RI = pts[half:]

        LI.sort(key=lambda A: A[1])
        RI.sort(key=lambda A: -A[1])

        for i in range(half):
            print(LI[i][2], RI[i][2])

if __name__ == "__main__":
    alif()
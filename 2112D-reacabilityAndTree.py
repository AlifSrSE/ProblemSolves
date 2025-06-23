# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2112/problem/D

def alif():
    TI = int(input())

    for _ in range(TI):
        ni = int(input())
        aidj = [[] for _ in range(ni + 1)]

        for _ in range(ni - 1):
            ui, vi = map(int, input().split())
            aidj[ui].append(vi)
            aidj[vi].append(ui)

        if ni == 2:
            print("NO")
            continue
        center = -1

        for i in range(1, ni + 1):
            if len(aidj[i]) == 2:
                center = i
                break
        
        if center == -1:
            print("NO")
            continue

        ui, wi = aidj[center][0], aidj[center][1]
        print("YES")
        ans = [(ui, center), (center, wi)]
        
        def dfsU(xi, pi, di):
            for yi in aidj[xi]:
                if yi == pi or (xi == ui and yi == center) or (xi == center and yi == ui):
                    continue
                if di % 2 == 0:
                    ans.append((xi, yi))
                else:
                    ans.append((yi, xi))
                dfsU(yi, xi, di + 1)
        dfsU(ui, center, 0)

        def dfsW(xi, pi, di):
            for yi in aidj[xi]:
                if yi == pi or (xi == wi and yi == center) or (xi == center and yi == wi):
                    continue
                if di % 2 == 0:
                    ans.append((yi, xi))
                else:
                    ans.append((xi, yi))
                dfsW(yi, xi, di + 1)
        dfsW(wi, center, 0)

        for xi, yi in ans:
            print(xi, yi)

if __name__ == "__main__":
    alif()
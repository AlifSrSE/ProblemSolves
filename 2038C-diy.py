# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    t = int(input()) 
    for _ in range(t):
        n = int(input()) 
        f = {}
        numbers = list(map(int, input().split()))  
        for x in numbers:
            if x in f:
                f[x] += 1
            else:
                f[x] = 1
        
        wat = []
        for key, value in f.items():
            value //= 2 
            if value:
                wat.append((key, value))
        
        wat.sort()
        cand = []
        for i in range(len(wat)):
            if i < 4 or i >= len(wat) - 4:
                cand.append(wat[i])

        area = -1
        ans = [-1, -1, -1, -1]

        for i1 in range(len(cand)):
            if cand[i1][1] > 0:
                cand[i1] = (cand[i1][0], cand[i1][1] - 1)
                for j1 in range(i1, len(cand)):
                    if cand[j1][1] > 0:
                        cand[j1] = (cand[j1][0], cand[j1][1] - 1)
                        for k1 in range(len(cand)):
                            if cand[k1][1] > 0:
                                cand[k1] = (cand[k1][0], cand[k1][1] - 1)
                                for l1 in range(k1, len(cand)):
                                    if cand[l1][1] > 0:
                                        cand[l1] = (cand[l1][0], cand[l1][1] - 1)
                                        here = (cand[j1][0] - cand[i1][0]) * 1 * (cand[l1][0] - cand[k1][0])
                                        if here > area:
                                            area = here
                                            ans = [cand[i1][0], cand[j1][0], cand[k1][0], cand[l1][0]]
                                        cand[l1] = (cand[l1][0], cand[l1][1] + 1)
                                cand[k1] = (cand[k1][0], cand[k1][1] + 1)
                        cand[j1] = (cand[j1][0], cand[j1][1] + 1)
                cand[i1] = (cand[i1][0], cand[i1][1] + 1)

        if area == -1:
            print("NO")
        else:
            print("YES")
            print(f"{ans[0]} {ans[2]} {ans[0]} {ans[3]} {ans[1]} {ans[2]} {ans[1]} {ans[3]}")

if __name__ == "__main__":
    solve()

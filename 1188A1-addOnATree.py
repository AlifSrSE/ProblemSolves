# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1188/problem/A1

def alif():
    n = int(input())
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        deg[x] += 1
        deg[y] += 1

    possible = True
    for p in range(1, n + 1):
        if deg[p] == 2:
            possible = False
            break
    
    print("YES" if possible else "NO")

if __name__ == "__main__":
    alif()

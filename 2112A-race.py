# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2112/problem/A

def alif():
    t = int(input())
    
    for _ in range(t):
        a, x, y = map(int, input().split())
        da1 = abs(a - x)
        da2 = abs(a - y)
        found = False

        for bob in range(1, 101):
            if bob == a:
                continue
            db1 = abs(bob - x)
            db2 = abs(bob - y)
            if db1 < da1 and db2 < da2:
                found = True
                break
        print("YES" if found else "NO")

if __name__ == "__main__":
    alif()
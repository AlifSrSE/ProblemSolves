# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1196/problem/C

def alif():
    q = int(input())
    for _ in range(q):
        n = int(input())
        xmin = -100000
        xmax = 100000
        ymin = -100000
        ymax = 100000
        
        for p in range(n):
            x, y, down, right, up, left = map(int, input().split())
            if down == 0:
                xmin = max(xmin, x)
            if up == 0:
                xmax = min(xmax, x)
            if left == 0:
                ymin = max(ymin, y)
            if right == 0:
                ymax = min(ymax, y)
        
        if xmax < xmin or ymax < ymin:
            print(0)
        else:
            print(1, xmin, ymin)

if __name__ == "__main__":
    alif()
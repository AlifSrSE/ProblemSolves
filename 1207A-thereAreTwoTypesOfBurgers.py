# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1207/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        b, p, f = map(int, input().split())
        h, c = map(int, input().split())
        
        profit = 0
        if h > c:
            hamburgers = min(b // 2, p)
            b -= hamburgers * 2
            profit += hamburgers * h
            chicken_burgers = min(b // 2, f)
            profit += chicken_burgers * c
        else:
            chicken_burgers = min(b // 2, f)
            b -= chicken_burgers * 2
            profit += chicken_burgers * c
            hamburgers = min(b // 2, p)
            profit += hamburgers * h
        
        print(profit)

if __name__ == "__main__":
    alif()
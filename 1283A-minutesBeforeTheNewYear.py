# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1283/problem/A

def alif():
    t = int(input())
    
    for _ in range(t):
        h, m = map(int, input().split())
        result = 24 * 60 - (h * 60 + m)
        print(result)

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2122/problem/A

def alif():
    ti = int(input())
    for _ in range(ti):
        ni, mi = map(int, input().split())
        
        if ni == 1 or mi == 1 or (ni == 2 and mi == 2):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    alif()
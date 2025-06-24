# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1238/problem/A

def alif():
    t = int(input())
    
    for _ in range(t):
        x, y = map(int, input().split())
        result = x - y != 1
        print("YES" if result else "NO")

if __name__ == "__main__":
    alif()
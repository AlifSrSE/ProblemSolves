# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1214/problem/B

def alif():
    b = int(input())
    g = int(input())
    n = int(input())
    
    result = min(b, n) - max(0, n - g) + 1
    print(result)

if __name__ == "__main__":
    alif()
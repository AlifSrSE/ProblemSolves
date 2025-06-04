# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1205/problem/A

def alif():
    n = int(input())
    
    if n % 2 != 0:
        print("YES")
        a = [0] * (2 * n)
        
        for p in range(n):
            if p % 2 != 0:
                a[p] = 2 * p + 2
                a[p + n] = 2 * p + 1
            else:
                a[p] = 2 * p + 1
                a[p + n] = 2 * p + 2
        
        print(*a)
    else:
        print("NO")

if __name__ == "__main__":
    alif()
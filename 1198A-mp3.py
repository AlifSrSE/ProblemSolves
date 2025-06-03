# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1198/problem/A

def alif():
    n, b_val = map(int, input().split())
    bits = (8 * b_val) // n
    range_val = 1 << bits
    a = list(map(int, input().split()))
    a.sort()
    
    chg = n
    for i in range(n):
        count = 0
        for j in range(n):
            if a[j] < a[i] or a[j] > a[i] + range_val - 1:
                count += 1
        chg = min(chg, count)
    
    print(chg)

if __name__ == "__main__":
    alif()
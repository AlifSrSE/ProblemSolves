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
        distinct = 1
        j = i
        while j < n - 1 and distinct < range_val:
            if a[j + 1] != a[j]:
                distinct += 1
            j += 1
        if distinct > range_val:
            continue
        count = i + (n - 1 - j)
        chg = min(chg, count)
    
    print(chg)

if __name__ == "__main__":
    alif()
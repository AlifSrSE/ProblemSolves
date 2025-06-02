# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1201/problem/C

def alif():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    mid_idx = n // 2
    res = a[mid_idx]
    
    for p in range(mid_idx, n - 1):
        diff = a[p + 1] - res
        dist = p + 1 - mid_idx 
        add = min(diff, k // dist)
        res += add
        k -= add * dist
        
        if k == 0:
            break
    elements_from_median_to_end = n - mid_idx
    res += k // elements_from_median_to_end
    
    print(res)

if __name__ == "__main__":
    alif()
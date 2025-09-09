# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    ok = True
    current_capacity = 0

    for i in range(n):
        current_capacity = b[i] - max(0, a[i] - current_capacity)
        if current_capacity < 0:
            ok = False
            break

    if not ok:
        print("NO")
        return
    
    l = 0
    r = b[0]
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        current_capacity = mid
        ok_cycle = True
        
        for i in range(n):
            current_capacity = b[i] - max(0, a[i] - current_capacity)
            if current_capacity < 0:
                ok_cycle = False
                break
            
        if ok_cycle:
            if current_capacity >= mid:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        else:
            l = mid + 1
            
    if ans != -1:
        print("YES")
    else:
        print("NO")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

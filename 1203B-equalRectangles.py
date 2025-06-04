# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1203/problem/B

def alif():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()

        left = 0
        right = 4 * n - 1
        area = -1
        possible = True

        while possible and (left < right):
            if a[left] != a[left + 1]:
                possible = False
            if a[right] != a[right - 1]:
                possible = False
            tst = a[left] * a[right]
            
            if area == -1:
                area = tst
            
            if tst != area:
                possible = False
            left += 2
            right -= 2
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    alif()
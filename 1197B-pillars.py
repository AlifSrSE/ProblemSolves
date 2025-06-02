# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1197/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    max_idx = 0
    
    for i in range(n):
        if a[i] > a[max_idx]:
            max_idx = i
    
    possible = True
    for i in range(1, max_idx + 1):
        if a[i] < a[i - 1]:
            possible = False
            break
    
    if possible:
        for i in range(max_idx + 1, n):
            if a[i] > a[i - 1]:
                possible = False
                break
    
    print("YES" if possible else "NO")

if __name__ == "__main__":
    alif()
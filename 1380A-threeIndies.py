# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    p = list(map(int, input().split()))
    found = False
    for i in range(1, n - 1):
        if p[i - 1] < p[i] and p[i] > p[i + 1]:
            print("YES")
            print(f"{i} {i + 1} {i + 2}")
            found = True
            break
    if not found:
        print("NO")

t = int(input())
for _ in range(t):
    alif()

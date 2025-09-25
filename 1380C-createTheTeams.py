# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    count = 0
    groups = 0
    for val in a:
        count += 1
        if count * val >= x:
            groups += 1
            count = 0
    print(groups)

t = int(input())
for _ in range(t):
    alif()

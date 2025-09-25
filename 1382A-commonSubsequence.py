# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = list(map(int, input().split()))
    
    found = False
    result = 0
    for x in b:
        if x in a:
            found = True
            result = x
            break
            
    if found:
        print("YES")
        print(1, result)
    else:
        print("NO")

t = int(input())
for _ in range(t):
    alif()

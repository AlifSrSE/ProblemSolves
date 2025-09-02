# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif():
    s = input()
    n = len(s)
    b = ""
    b += s[0]
    
    for i in range(1, n - 1, 2):
        b += s[i]

    b += s[n - 1]
    print(b)

t = int(input())
for _ in range(t):
    alif()
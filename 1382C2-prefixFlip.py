# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    a = input()
    b = input()
    moves = []
    one = (a[0] == '1')

    for p in range(1, n):
        if a[p - 1] != a[p]:
            moves.append(p)
            one = not one

    for p in range(n - 1, -1, -1):
        if (b[p] == '1' and one) or (b[p] == '0' and not one):
            continue
        moves.append(p + 1)
        one = not one

    print(len(moves), *moves)

t = int(input())
for _ in range(t):
    alif()

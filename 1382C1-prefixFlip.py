# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    a = input()
    b = input()
    
    moves = []
    
    for i in range(n):
        if a[i] == b[i]:
            continue
        
        moves.append(i + 1)
        moves.append(1)
        moves.append(i + 1)
    
    print(len(moves), *moves)

t = int(input())
for _ in range(t):
    alif()

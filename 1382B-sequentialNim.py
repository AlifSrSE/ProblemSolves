# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    piles = list(map(int, input().split()))
    first_player_turn = 0
    found_gt1 = False
    
    for pile in piles:
        if pile > 1:
            found_gt1 = True
            break
        elif not found_gt1:
            first_player_turn = 1 - first_player_turn
    
    if found_gt1:
        if first_player_turn == 1:
            print("Second")
        else:
            print("First")
    else:
        if n % 2 == 1:
            print("First")
        else:
            print("Second")

t = int(input())
for _ in range(t):
    alif()

# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    s = input()
    n = len(s)

    for k in range(n):
        l, r = k, k
        winner = "Ann"
        
        def can_move(curr_l, curr_r, new_l, new_r):
            if new_l <= curr_l and new_r >= curr_r:
                if s[new_l:new_r + 1] < s[curr_l:curr_r + 1]:
                    return True
            return False

        def find_winner(curr_l, curr_r, turn):
            nonlocal s, n

            for new_l in range(curr_l + 1):
                for new_r in range(curr_r, n):
                    if can_move(curr_l, curr_r, new_l, new_r):
                        if turn == "Mike":
                            return find_winner(new_l, new_r, "Ann")
                        else:
                            return find_winner(new_l, new_r, "Mike")

            return turn

        winner = find_winner(l, r, "Mike")
        print(winner)

solve()
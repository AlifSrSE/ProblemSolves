# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1229/problem/A

import sys

def arrogant(ind, team):
    if team[ind] < 0:
        return False

    current_player_skill = team[ind]

    for p in range(len(team)):
        if team[p] < 0:
            continue
        if p == ind:
            continue

        other_player_skill = team[p]
        better = False 
        temp_a = current_player_skill
        temp_b = other_player_skill

        while temp_a > 0 or temp_b > 0:
            if (temp_a & 1) and not (temp_b & 1):
                better = True
                break
            temp_a >>= 1
            temp_b >>= 1
            
        if not better:
            return False
    return True

def alif():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    total_sum_bonus = sum(b)
    active_player_count = n
    done = False

    while not done:
        done = True
        for p in range(n):
            if a[p] < 0:
                continue
            if arrogant(p, a):
                done = False
                active_player_count -= 1
                a[p] = -1
                total_sum_bonus -= b[p]

    if active_player_count > 1:
        sys.stdout.write(f"{total_sum_bonus}\n")
    else:
        sys.stdout.write("0\n")

if __name__ == "__main__":
    alif()
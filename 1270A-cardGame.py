# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1270/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, a_count, b_count = map(int, sys.stdin.readline().split())
        first_player_has_n = False
        first_player_numbers = list(map(int, sys.stdin.readline().split()))
        
        for x in first_player_numbers:
            if x == n:
                first_player_has_n = True
        
        second_player_numbers = list(map(int, sys.stdin.readline().split()))
        sys.stdout.write("YES\n" if first_player_has_n else "NO\n")

if __name__ == "__main__":
    alif()
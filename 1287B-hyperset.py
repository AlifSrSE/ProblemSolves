# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1287/problem/B

import sys

def alif():
    try:
        n, k = map(int, sys.stdin.readline().split())
        cards = []
        card_set = set()

        for _ in range(n):
            card_str = sys.stdin.readline().strip()
            cards.append(card_str)
            card_set.add(card_str)
    except (IOError, ValueError):
        return

    set_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            card1 = cards[i]
            card2 = cards[j]
            required_card_parts = []

            for feature_index in range(k):
                c1 = card1[feature_index]
                c2 = card2[feature_index]
                
                if c1 == c2:
                    required_card_parts.append(c1)
                else:
                    if 'S' not in (c1, c2):
                        required_card_parts.append('S')
                    elif 'E' not in (c1, c2):
                        required_card_parts.append('E')
                    else:
                        required_card_parts.append('T')

            required_card_str = "".join(required_card_parts)
            if required_card_str in card_set:
                set_count += 1
                
    print(set_count // 3)

if __name__ == "__main__":
    alif()
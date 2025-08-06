# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1272/C

import sys

def alif():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    N_ALPHABET = 26
    allowed_chars = [False] * N_ALPHABET
    input_allowed_chars = sys.stdin.readline().split()

    for char_val in input_allowed_chars:
        allowed_chars[ord(char_val) - ord('a')] = True
    
    lengths_of_allowed_blocks = []
    current_consecutive_count = 0
    
    for p in range(n):
        if allowed_chars[ord(s[p]) - ord('a')]:
            current_consecutive_count += 1
        else:
            lengths_of_allowed_blocks.append(current_consecutive_count)
            current_consecutive_count = 0

    lengths_of_allowed_blocks.append(current_consecutive_count)
    total_pairs = 0

    for length in lengths_of_allowed_blocks:
        total_pairs += length * (length + 1) // 2
    
    sys.stdout.write(f"{total_pairs}\n")

if __name__ == "__main__":
    alif()
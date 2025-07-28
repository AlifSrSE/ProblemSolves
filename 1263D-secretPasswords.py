# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1263/problem/D

import sys

N_ALPHABET = 26
parent = list(range(N_ALPHABET))

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_j] = root_i

def alif():
    global parent

    n = int(sys.stdin.readline())
    parent = list(range(N_ALPHABET)) 
    seen_char_flag = [False] * N_ALPHABET

    for _ in range(n):
        s = sys.stdin.readline().strip()
        current_string_chars_indices = []

        for char_code in s:
            idx = ord(char_code) - ord('a')
            seen_char_flag[idx] = True
            current_string_chars_indices.append(idx)
        
        if current_string_chars_indices:
            first_char_root = find(current_string_chars_indices[0])
            for i in range(1, len(current_string_chars_indices)):
                union(first_char_root, current_string_chars_indices[i])
    distinct_components_count = 0

    for i in range(N_ALPHABET):
        if seen_char_flag[i] and parent[i] == i:
            distinct_components_count += 1
            
    sys.stdout.write(f"{distinct_components_count}\n")

if __name__ == "__main__":
    alif()
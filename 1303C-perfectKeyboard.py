# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1303/problem/C

import sys
from collections import defaultdict

def alif():
    s = sys.stdin.readline().strip()
    if not s or len(set(s)) == 1:
        print("YES")
        print("abcdefghijklmnopqrstuvwxyz")
        return

    adj = defaultdict(set)
    possible = True
    for i in range(len(s) - 1):
        u, v = s[i], s[i+1]
        adj[u].add(v)
        adj[v].add(u)
    start_node = None
    all_chars = set()

    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        if len(adj[char]) > 2:
            possible = False
            break
        if len(adj[char]) == 1:
            if start_node is None:
                start_node = char
            else:
                pass

    if not possible:
        print("NO")
        return
    
    if start_node is None:
        possible = False
        
    if not possible:
        print("NO")
        return

    result = ""
    visited = set()
    current_char = start_node
    
    while current_char is not None and current_char not in visited:
        result += current_char
        visited.add(current_char)
        next_char = None
        for neighbor in adj[current_char]:
            if neighbor not in visited:
                next_char = neighbor
                break
        current_char = next_char

    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        if char not in visited:
            result += char
            
    print("YES")
    print(result)

def rahman():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        t = 0
    
    for _ in range(t):
        alif()

if __name__ == "__main__":
    rahman()
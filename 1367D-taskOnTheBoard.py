# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from collections import Counter

def alif():
    s = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    counts = Counter(s)
    
    t = [''] * m
    unfilled = list(range(m))
    
    char_code = ord('z')
    
    while True:
        zero_indices = []
        for i in unfilled:
            if b[i] == 0:
                zero_indices.append(i)
        
        if not zero_indices:
            break
        
        current_char = chr(char_code)
        
        while counts[current_char] < len(zero_indices):
            char_code -= 1
            current_char = chr(char_code)
        
        for i in zero_indices:
            t[i] = current_char
            
        next_unfilled = []
        for i in unfilled:
            if i not in zero_indices:
                for j in zero_indices:
                    b[i] -= abs(i - j)
                next_unfilled.append(i)
        unfilled = next_unfilled
        
        char_code -= 1
        
    print("".join(t))

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        alif()

if __name__ == "__main__":
    main()

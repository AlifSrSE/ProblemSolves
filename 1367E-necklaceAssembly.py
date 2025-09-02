# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from collections import Counter
from math import gcd

def alif():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    counts = Counter(s)
    
    for l in range(n, 0, -1):
        g = gcd(l, k)
        group_size = l // g
        
        total_groups_available = 0
        for count in counts.values():
            total_groups_available += count // group_size
            
        if total_groups_available >= g:
            print(l)
            return

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

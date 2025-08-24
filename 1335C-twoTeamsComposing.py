# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from collections import Counter

def alif():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            n = int(sys.stdin.readline())
            if n == 0:
                sys.stdout.write("0\n")
                continue
            
            skills = list(map(int, sys.stdin.readline().split()))
            skill_counts = Counter(skills)
            d = len(skill_counts)
            mx = max(skill_counts.values())
            
            result = 0
            if d == mx:
                result = d - 1
            else:
                result = min(d, mx)
            
            sys.stdout.write(str(result) + '\n')
    except (IOError, ValueError) as e:
        pass

if __name__ == "__main__":
    alif()
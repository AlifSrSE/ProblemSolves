# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

s1 = input().strip()
s2 = input().strip()

from collections import defaultdict

def can_compose(s1, s2):
    s2_counts = defaultdict(int)
    for char in s2:
        if char != ' ':
            s2_counts[char] += 1
    
    s1_counts = defaultdict(int)
    for char in s1:
        if char != ' ':
            s1_counts[char] += 1
    
    for char, count in s2_counts.items():
        if s1_counts[char] < count:
            return False
    return True

if can_compose(s1, s2):
    print("YES")
else:
    print("NO")
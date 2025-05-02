# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1167/problem/A

def compute_pair_num(x):
    return x * (x - 1) // 2

def alif(names):
    first_letter_to_count = {}
    for name in names:
        first_letter = name[0]
        first_letter_to_count[first_letter] = first_letter_to_count.get(first_letter, 0) + 1
    
    return sum(compute_pair_num(count // 2) + compute_pair_num(count - count // 2) 
               for count in first_letter_to_count.values())

n = int(input())
names = [input() for _ in range(n)]
print(alif(names))
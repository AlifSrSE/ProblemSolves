# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
t = int(input())
for _ in range(t):
    s = input()
    r_count = s.count('R')
    p_count = s.count('P')
    s_count = s.count('S')
    if p_count >= r_count and p_count >= s_count:
        print('S' * len(s))
    elif r_count >= p_count and r_count >= s_count:
        print('P' * len(s))
    else:
        print('R' * len(s))

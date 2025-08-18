# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1320/problem/A

def alif():
    n = int(input())
    b = list(map(int, input().split()))

    diff_map = {}
    max_sum = 0

    for i in range(n):
        diff = b[i] - i
        if diff in diff_map:
            diff_map[diff] += b[i]
        else:
            diff_map[diff] = b[i]
        
        if diff_map[diff] > max_sum:
            max_sum = diff_map[diff]
    
    print(max_sum)

alif()
# Author : AlifSrSE
# Date : 2025-02-16
# Problem link : https://codeforces.com/contest/4691165/problem/B

def max_training_days(n, contests):
    contests.sort()
    day = 1
    
    for problems in contests:
        if problems >= day:
            day += 1
    
    return day - 1

n = int(input().strip())
contests = list(map(int, input().strip().split()))
result = max_training_days(n, contests)
print(result)
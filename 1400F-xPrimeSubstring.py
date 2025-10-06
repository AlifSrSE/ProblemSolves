# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def get_divisors(x):
    divisors = []
    for d in range(1, x):
        if x % d == 0:
            divisors.append(d)
    return divisors

def is_x_prime(s, l, r, x, divisors):
    substring_sum = sum(int(s[i]) for i in range(l, r + 1))
    if substring_sum != x:
        return False
    for l2 in range(l, r + 1):
        for r2 in range(l2, r + 1):
            if l2 == l and r2 == r:
                continue
            sub_sum = sum(int(s[i]) for i in range(l2, r2 + 1))
            if sub_sum != x and sub_sum in divisors:
                return False
    return True

def alif():
    s = input().strip()
    x = int(input())
    n = len(s)
    divisors = get_divisors(x)
    x_prime_substrings = []

    for l in range(n):
        for r in range(l, n):
            if is_x_prime(s, l, r, x, divisors):
                x_prime_substrings.append((l, r))
    
    if not x_prime_substrings:
        print(0)
        return
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        can_keep = True
        for l, r in x_prime_substrings:
            if r == i - 1:
                valid = True
                for j in range(l, r + 1):
                    if j < i - 1 and dp[j + 1] == float('inf'):
                        valid = False
                        break
                if valid:
                    can_keep = False
                    break
        if can_keep:
            dp[i] = dp[i - 1]
            
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
    print(dp[n])

alif()
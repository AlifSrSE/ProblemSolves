# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    a = list(map(int, input().split()))
    dp = {}
    
    def can_do_range(l, r, a_temp):
        for i in range(l, r + 1):
            if a_temp[i] < 1:
                return False
        return True
    
    def solve(l, r, a_temp):
        if l > r:
            return 0
        state = (l, r, tuple(a_temp[l:r+1]))
        if state in dp:
            return dp[state]
        ans = float('inf')
        
        if can_do_range(l, r, a_temp):
            new_a = a_temp[:]
            for i in range(l, r + 1):
                new_a[i] -= 1
            ans = min(ans, 1 + solve(l, r, new_a))
        
        for i in range(l, r + 1):
            if a_temp[i] > 0:
                new_a = a_temp[:]
                operations = new_a[i]
                new_a[i] = 0
                ans = min(ans, operations + solve(l, i - 1, new_a) + solve(i + 1, r, new_a))
        
        for k in range(l, r):
            ans = min(ans, solve(l, k, a_temp) + solve(k + 1, r, a_temp))
        
        dp[state] = ans
        return ans
    
    a = [0] + a
    result = solve(1, n, a)
    print(result)

alif()
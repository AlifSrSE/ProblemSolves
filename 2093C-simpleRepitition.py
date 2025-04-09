# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def solve():
    x, k = map(int, input().split())
    result = "YES" if (k == 1 and is_prime(x)) or (k == 2 and x == 1) else "NO"
    print(result)
 
t = int(input())
for _ in range(t):
    solve()
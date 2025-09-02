# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
 
def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = sorted(a)
    b_index = {val: i for i, val in enumerate(b)}
    dp = {}
    max_len = 0
    
    for val in a:
        idx = b_index[val]
        dp[idx] = dp.get(idx - 1, 0) + 1
        max_len = max(max_len, dp[idx])
    print(n - max_len)
 
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()
 
if __name__ == "__main__":
    main()
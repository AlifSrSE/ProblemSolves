# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    MOD = 1000000007
    n_str = sys.stdin.read().strip()

    if not n_str:
        return
    n = int(n_str)
    f = 1
    
    for p in range(1, n + 1):
        f = (f * p) % MOD
    w = 1

    for p in range(1, n):
        w = (w * 2) % MOD
    res = (f - w + MOD) % MOD
    sys.stdout.write(str(res) + '\n')

alif()

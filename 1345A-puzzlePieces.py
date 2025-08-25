# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        nm_str = sys.stdin.readline()
        if not nm_str:
            continue
        
        n, m = map(int, nm_str.split())
        
        if n == 1 or m == 1 or (n == 2 and m == 2):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()
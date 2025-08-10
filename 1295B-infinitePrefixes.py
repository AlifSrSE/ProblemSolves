# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1295/problem/B

import sys

def alif():
    try:
        n, x = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return

    cnt = {}
    balance = 0

    for char in s:
        if char == '0':
            balance += 1
        else:
            balance -= 1
        cnt[balance] = cnt.get(balance, 0) + 1
    
    total_balance_change = balance
    if total_balance_change == 0:
        if x == 0:
            print("-1")
            return
        
        if x in cnt:
            print("-1")
        else:
            print("0")
        return
    
    res = 0
    if x == 0:
        res += 1

    for prefix_balance, count in cnt.items():
        remaining = x - prefix_balance
        
        if remaining % total_balance_change == 0:
            if remaining // total_balance_change >= 0:
                res += count
    
    print(res)

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
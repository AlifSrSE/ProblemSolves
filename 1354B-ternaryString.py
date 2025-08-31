# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    s = sys.stdin.readline().strip()
    last = {'1': -1, '2': -1, '3': -1}
    min_len = len(s) + 1
    
    for i in range(len(s)):
        last[s[i]] = i
        
        if last['1'] != -1 and last['2'] != -1 and last['3'] != -1:
            prev = min(last['1'], last['2'], last['3'])
            current_len = i - prev + 1
            min_len = min(min_len, current_len)
    
    if min_len == len(s) + 1:
        print(0)
    else:
        print(min_len)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
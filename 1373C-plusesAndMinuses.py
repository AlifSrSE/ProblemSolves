# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    s = sys.stdin.readline().strip()
    balance = 0
    ans = len(s)
    needed_add = 0
    
    for i in range(len(s)):
        if s[i] == '+':
            balance += 1
        else:
            balance -= 1
            
        if balance + needed_add < 0:
            needed_add += 1
            ans += (i + 1)
            
    print(ans)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

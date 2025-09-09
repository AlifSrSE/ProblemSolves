# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    current_balance = 0
    min_balance = 0
    
    for char in s:
        if char == '(':
            current_balance += 1
        else:
            current_balance -= 1
        
        if current_balance < min_balance:
            min_balance = current_balance
            
    print(-min_balance)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    s = sys.stdin.readline().strip()
    zeros = s.count('0')
    ones = s.count('1')
    
    removable = min(zeros, ones)
    
    if removable % 2 == 1:
        print("DA")
    else:
        print("NET")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

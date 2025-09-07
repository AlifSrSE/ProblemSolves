# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    start = -1
    end = -1
    
    for i in range(n):
        if a[i] != i + 1:
            if start == -1:
                start = i
            end = i
            
    if start == -1:
        print(0)
    else:
        is_sorted_middle = True
        for i in range(start, end + 1):
            if a[i] == i + 1:
                is_sorted_middle = False
                break
        
        if is_sorted_middle:
            print(1)
        else:
            print(2)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()

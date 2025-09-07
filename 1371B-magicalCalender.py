# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, r = map(int, sys.stdin.readline().split())
        
        if r < n:
            ans = r * (r + 1) // 2
        else:
            ans = (n - 1) * n // 2 + 1
            
        print(ans)

if __name__ == '__main__':
    main()

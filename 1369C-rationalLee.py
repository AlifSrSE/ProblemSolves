# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        w = list(map(int, sys.stdin.readline().split()))
        a.sort()
        w.sort(reverse=True)
        
        total_sum = 0
        
        for i in range(k):
            total_sum += a[n - 1 - i]
            
        left_idx = 0
        for i in range(k):
            if w[i] == 1:
                total_sum += a[n - 1 - i]
            else:
                total_sum += a[left_idx]
                left_idx += w[i] - 1
        
        sys.stdout.write(str(total_sum) + '\n')

if __name__ == '__main__':
    main()

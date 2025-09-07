# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        
        odd_indices = []
        even_indices = []
        
        for i, val in enumerate(a):
            if val % 2 == 1:
                odd_indices.append(i + 1)
            else:
                even_indices.append(i + 1)
        
        pairs_count = n - 1
        
        for i in range(0, len(odd_indices) - 1, 2):
            if pairs_count > 0:
                print(odd_indices[i], odd_indices[i+1])
                pairs_count -= 1
        
        for i in range(0, len(even_indices) - 1, 2):
            if pairs_count > 0:
                print(even_indices[i], even_indices[i+1])
                pairs_count -= 1

if __name__ == '__main__':
    main()

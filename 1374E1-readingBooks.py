# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from itertools import accumulate

def alif():
    n, k = map(int, sys.stdin.readline().split())
    a_books = []
    b_books = []
    both_books = []
    
    for _ in range(n):
        t, x, y = map(int, sys.stdin.readline().split())
        if x == 1 and y == 1:
            both_books.append(t)
        elif x == 1:
            a_books.append(t)
        elif y == 1:
            b_books.append(t)
            
    if len(a_books) + len(both_books) < k or len(b_books) + len(both_books) < k:
        print(-1)
        return

    a_books.sort()
    b_books.sort()
    both_books.sort()

    a_prefix = [0] + list(accumulate(a_books))
    b_prefix = [0] + list(accumulate(b_books))
    both_prefix = [0] + list(accumulate(both_books))
    min_time = float('inf')
    
    for i in range(min(k, len(both_books)) + 1):
        required_individual = k - i
        if required_individual <= len(a_books) and required_individual <= len(b_books):
            current_time = both_prefix[i] + a_prefix[required_individual] + b_prefix[required_individual]
            min_time = min(min_time, current_time)
            
    print(min_time)

if __name__ == "__main__":
    alif()

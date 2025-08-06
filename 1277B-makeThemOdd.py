# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1277/B

import sys
import heapq

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        unique_evens = set() 
        input_numbers = list(map(int, sys.stdin.readline().split()))

        for x in input_numbers:
            if x % 2 == 0:
                unique_evens.add(x)
        s_heap = []

        for num in unique_evens:
            heapq.heappush(s_heap, -num)
        cnt = 0
        
        while s_heap:
            x_neg = heapq.heappop(s_heap)
            x = -x_neg
            cnt += 1
            x //= 2
            
            if x % 2 == 0 and x not in unique_evens:
                unique_evens.add(x)
                heapq.heappush(s_heap, -x)
        sys.stdout.write(f"{cnt}\n")

if __name__ == "__main__":
    alif()
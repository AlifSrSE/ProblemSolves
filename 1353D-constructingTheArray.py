# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import heapq

def alif():
    n = int(sys.stdin.readline())
    result_array = [0] * n
    pq = []
    heapq.heappush(pq, (-n, 0, n - 1))
    count = 1
    
    while pq:
        neg_length, left, right = heapq.heappop(pq)
        mid = (left + right) // 2
        result_array[mid] = count
        count += 1
        left_length = mid - left
        right_length = right - mid
        
        if left_length > 0:
            heapq.heappush(pq, (-left_length, left, mid - 1))
        
        if right_length > 0:
            heapq.heappush(pq, (-right_length, mid + 1, right))
    print(*result_array)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
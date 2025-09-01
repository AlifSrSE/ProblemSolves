# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import math

def alif():
    n, m = map(int, sys.stdin.readline().split())
    given_nums = []
    for _ in range(n):
        s = sys.stdin.readline().strip()
        given_nums.append(int(s, 2))
    
    given_nums.sort()
    
    total_count = 1 << m
    missing_count = total_count - n
    median_index = (missing_count - 1) // 2
    
    low = 0
    high = total_count - 1
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        count_given_le_mid = 0
        for num in given_nums:
            if num <= mid:
                count_given_le_mid += 1
            else:
                break
        
        missing_le_mid = (mid + 1) - count_given_le_mid
        
        if missing_le_mid <= median_index:
            low = mid + 1
        else:
            result = mid
            high = mid - 1
    
    binary_result = bin(result)[2:].zfill(m)
    print(binary_result)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
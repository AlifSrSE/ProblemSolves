# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def max_ones_after_flip(n, arr):
    original_ones = sum(arr)
    
    if n == 1:
        return 1 - arr[0]  
    
    current_diff = float('-inf')
    max_diff = float('-inf')
    
    for i in range(n):
        val = 1 - arr[i] * 2
        current_diff = max(val, current_diff + val)
        max_diff = max(max_diff, current_diff)
    
    return original_ones + max_diff

n = int(input())
arr = list(map(int, input().split()))

print(max_ones_after_flip(n, arr))
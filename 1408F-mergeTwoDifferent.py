# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def merge_pow2_block(start, size, pairs):
    if size <= 1:
        return
    
    half = size // 2
    
    merge_pow2_block(start, half, pairs)
    merge_pow2_block(start + half, half, pairs)
    
    for i in range(half):
        pairs.append((start + i, start + half + i))

def alif():
    n = int(sys.stdin.read())
    pairs = []
    
    if n == 1:
        print(0)
        return
    k = 1

    while (k * 2) <= n:
        k *= 2
        
    def recursive_merge(start, size):
        if size <= 1:
            return
        half = size // 2

        recursive_merge(start, half)
        recursive_merge(start + half, half)
        
        for i in range(half):
            pairs.append((start + i, start + half + i))
    current_size = 1

    while current_size * 2 <= n:
        current_size *= 2
    K = current_size
    K = 1

    while K * 2 <= n:
        K *= 2
        
    recursive_merge(1, K)
    R = n - K
    start_idx = 1
    temp_n = n
    block_size = 1

    while block_size * 2 <= n:
        block_size *= 2
    while start_idx + block_size <= n + 1:
        recursive_merge(start_idx, block_size)
        start_idx += block_size
    
    M = start_idx - 1
    R = n - M
    
    if R > 0:
        K_R = 1
        while K_R * 2 <= R:
            K_R *= 2
            
        
        current_R_start = M + 1
        current_M_start = M - R + 1
        
        temp_R = R
        while temp_R > 0:
            block = 1
            while block * 2 <= temp_R:
                block *= 2
            
            for i in range(block):
                pairs.append((current_M_start + i, current_R_start + i))
            
            current_M_start += block
            current_R_start += block
            temp_R -= block

    
    print(len(pairs))
    for x, y in pairs:
        print(f"{x} {y}")

alif()
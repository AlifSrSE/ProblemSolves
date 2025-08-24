# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

from heapq import heapify, heappush, heappop

def alif(h, g, a):
    n = (1 << h) - 1
    m = (1 << g) - 1
    operations = 2**h - 2**g
    heap = [(-a[i-1], i) for i in range(1, n+1) if a[i-1] != 0]
    heapify(heap)
    used = set()
    ans = []
    
    for _ in range(operations):
        val, idx = heappop(heap)
        val = -val
        ans.append(idx)
        used.add(idx)
        
        curr = idx
        while curr <= n:
            left = curr * 2
            right = curr * 2 + 1
            next_idx = 0
            next_val = 0
            if left <= n and left not in used and (right > n or right in used or (right <= n and a[left-1] < a[right-1])):
                next_idx = left
                next_val = a[left-1]
            elif right <= n and right not in used:
                next_idx = right
                next_val = a[right-1]
            
            a[curr-1] = next_val
            if next_idx:
                used.add(next_idx)
                heappush(heap, (-next_val, curr))
            curr = next_idx
    
    total_sum = sum(a[i] for i in range(m) if a[i] != 0)
    return total_sum, ans

t = int(input())
for _ in range(t):
    h, g = map(int, input().split())
    a = list(map(int, input().split()))
    total_sum, operations = alif(h, g, a)
    print(total_sum)
    print(*operations)
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif(n, k, a):
    a.sort()
    min_moves = float('inf')
    
    for target in range(a[0], a[-1] + 1):
        moves = 0
        for i in range(n):
            if i < n - k:
                moves += target - a[i]
            elif i >= n - k and a[i] < target:
                moves += target - a[i]
            elif i >= n - k and a[i] > target:
                moves += a[i] - target
        min_moves = min(min_moves, moves)
    
    return min_moves

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(alif(n, k, a))
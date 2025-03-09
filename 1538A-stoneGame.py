def min_moves(n, stones):
    min_power = min(stones)
    max_power = max(stones)
    min_index = stones.index(min_power)
    max_index = stones.index(max_power)

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    leftmost = max_index + 1
    rightmost = n - min_index
    mixed = min_index + 1 + (n - max_index)
    
    return min(leftmost, rightmost, mixed)

t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    stones = list(map(int, input().strip().split()))
    results.append(min_moves(n, stones))

for result in results:
    print(result)
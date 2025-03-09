def max_sum_and_min_operations(n, array):
    max_sum = sum(abs(x) for x in array)
    min_operations = 0
    i = 0
    
    while i < n:
        if array[i] < 0:
            min_operations += 1
            while i < n and array[i] < 0:
                i += 1
        while i < n and array[i] >= 0:
            i += 1
    
    return max_sum, min_operations

t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    array = list(map(int, input().strip().split()))
    results.append(max_sum_and_min_operations(n, array))

for result in results:
    print(result[0], result[1])
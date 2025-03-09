def sum_in_binary_tree(n):
    total_sum = 0
    while n > 0:
        total_sum += n
        n //= 2
    return total_sum

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(sum_in_binary_tree(n))
    
    for result in results:
        print(result)
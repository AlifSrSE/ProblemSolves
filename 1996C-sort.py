def min_operations_to_sort_substrings(t, test_cases):
    results = []
    
    for case in test_cases:
        n, q, a, b, queries = case
        for l, r in queries:
            sub_a = a[l - 1:r]
            sub_b = b[l - 1:r]

            sorted_a = sorted(sub_a)
            sorted_b = sorted(sub_b)

            operations = sum(1 for x, y in zip(sorted_a, sorted_b) if x != y)
            results.append(operations)
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        a = data[index]
        b = data[index + 1]
        index += 2
        queries = []
        for _ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            queries.append((l, r))
            index += 2
        test_cases.append((n, q, a, b, queries))
    
    results = min_operations_to_sort_substrings(t, test_cases)
    for result in results:
        print(result)
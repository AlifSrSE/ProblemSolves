def minimal_square(t, test_cases):
    results = []
    for a, b in test_cases:
        side1 = max(2*a, b)
        side2 = max(a, 2*b)
        side3 = max(a + b, max(a, b))
        min_side = min(side1, side2, side3)
        area = min_side * min_side
        results.append(area)
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = minimal_square(t, test_cases)
for result in results:
    print(result)
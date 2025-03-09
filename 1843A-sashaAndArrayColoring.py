def solve(a):
    a.sort()
    
    result = 0
    i = 0
    j = len(a) - 1
    while i < j:
        result += a[j] - a[i]
        i += 1
        j -= 1
    
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(solve(a))
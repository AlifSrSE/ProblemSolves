def min_coins_to_add(n, k, chests):
    chests.sort(reverse=True)  # Sort chests in descending order
    total = sum(chests)
    
    if total >= k:
        prefix_sum = 0
        for i in range(n):
            prefix_sum += chests[i]
            if prefix_sum >= k:
                return max(0, k - prefix_sum + chests[i])
        return 0
    
    return k - total  # Minimum coins needed to make total at least k

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        chests = list(map(int, input().split()))
        results.append(min_coins_to_add(n, k, chests))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()

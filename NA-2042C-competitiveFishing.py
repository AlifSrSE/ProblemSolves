def min_groups(t, test_cases):
    results = []
    
    for n, k, fishes in test_cases:
        alice_score = 0
        bob_score = 0
        groups = 0
        alice_count = 0
        bob_count = 0
        for i in range(n):
            if fishes[i] == '0':
                alice_count += 1
            else:
                bob_count += 1
            if i == n - 1 or fishes[i] != fishes[i + 1]:
                groups += 1
                if fishes[i] == '0':
                    alice_score += (groups - 1) * alice_count
                else:
                    bob_score += (groups - 1) * bob_count
                alice_count = 0
                bob_count = 0

        score_difference = bob_score - alice_score
        
        if score_difference >= k:
            results.append(groups)
        else:
            additional_needed = k - score_difference
            if additional_needed > (n - groups):
                results.append(-1)
            else:
                results.append(groups + additional_needed)
    
    return results

def main():
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n, k = map(int, input().split())
        fishes = input().strip()
        test_cases.append((n, k, fishes))
    
    output = min_groups(t, test_cases)
    for result in output:
        print(result)

if __name__ == "__main__":
    main()
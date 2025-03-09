from collections import Counter

def alice_score(n, colors):
    color_count = Counter(colors)
    unique_colors = set(colors)
    sorted_colors = sorted(color_count.items(), key=lambda x: -x[1])  # Sort by frequency descending
    
    alice_colors = set()
    alice_full_colors = set()
    bob_turn = False  # Alice starts first
    taken = []
    
    for color, count in sorted_colors:
        taken.extend([color] * count)
    
    for i in range(n):
        color = taken[i]
        if not bob_turn:
            alice_colors.add(color)
            color_count[color] -= 1
            if color_count[color] == 0:
                alice_full_colors.add(color)
        bob_turn = not bob_turn
    
    return len(alice_colors) + len(alice_full_colors)

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        colors = list(map(int, input().split()))
        results.append(alice_score(n, colors))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()
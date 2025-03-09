import sys
from collections import Counter

def solve(c):
    color_to_count = Counter(c)
    
    sorted_colors = sorted(c, key=lambda color: (color_to_count[color], color))
    
    result = 0
    for i in range(0, len(sorted_colors), 2):
        if i == 0 or sorted_colors[i] != sorted_colors[i - 2]:
            result += 1
            
            if color_to_count[sorted_colors[i]] == 1:
                result += 1
    
    return result

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        c = list(map(int, input().split()))
        print(solve(c))

if __name__ == "__main__":
    main()

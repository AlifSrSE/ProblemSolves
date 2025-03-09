def can_pass_all_levels(n, x_levels, y_levels):
    all_levels = set(x_levels).union(set(y_levels))
    if len(all_levels) == n:
        return "I become the guy."
    else:
        return "Oh, my keyboard!"
    
n = int(input())
p_levels = list(map(int, input().split()))[1:]  
q_levels = list(map(int, input().split()))[1:]  
result = can_pass_all_levels(n, p_levels, q_levels)
print(result)
def longest_sushi_segment(n, sushi_types):
    max_length = 0
    current_tuna = 0
    current_eel = 0
    prev_type = sushi_types[0]
    
    for i in range(n):
        if sushi_types[i] == 1:
            if prev_type == 2:
                max_length = max(max_length, 2 * min(current_tuna, current_eel))
                current_tuna = 0
            current_tuna += 1
        else:
            if prev_type == 1:
                max_length = max(max_length, 2 * min(current_tuna, current_eel))
                current_eel = 0
            current_eel += 1
        prev_type = sushi_types[i]
    
    max_length = max(max_length, 2 * min(current_tuna, current_eel))
    return max_length

n = int(input().strip())
sushi_types = list(map(int, input().strip().split()))
print(longest_sushi_segment(n, sushi_types))
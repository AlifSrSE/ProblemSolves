def earliest_time_to_reach(t, sx, sy, ex, ey, wind_directions):
    x, y = sx, sy
    
    for i in range(t):
        if x == ex and y == ey:
            return i
        
        if wind_directions[i] == 'E' and x < ex:
            x += 1
        elif wind_directions[i] == 'W' and x > ex:
            x -= 1
        elif wind_directions[i] == 'N' and y < ey:
            y += 1
        elif wind_directions[i] == 'S' and y > ey:
            y -= 1
    
    if x == ex and y == ey:
        return t
    else:
        return -1
    

t, sx, sy, ex, ey = map(int, input().strip().split())
wind_directions = input().strip()
result = earliest_time_to_reach(t, sx, sy, ex, ey, wind_directions)

print(result)
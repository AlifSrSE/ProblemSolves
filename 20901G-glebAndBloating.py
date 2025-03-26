# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/G
 
def solve():
    s, k = map(int, input().split())
    
    for t in range(k + 1):
        final_power = max(1, k - t)
        p = [max(1, k - i) for i in range(t + 1)]
        
        if t == 0:
            if s % k == 0:
                print(k)
                return
            continue
        
        a = [1] * t
        pos = 0
        dist = 0
        positions = [0]
        valid = True
        
        for i in range(t):
            if i % 2 == 0:
                pos += a[i] * p[i]
            else:
                pos -= a[i] * p[i]
            positions.append(pos)
            if pos < 0 or pos > s:
                valid = False
                break
            dist += (-1)**i * a[i] * p[i]
        
        if not valid:
            def try_combinations(segment, pos, dist, positions, a):
                if segment == t:
                    a_t = (s - dist) / ((-1)**t * p[t])
                    if a_t != int(a_t) or a_t < 1:
                        return False
                    a_t = int(a_t)
                    pos_final = pos + (-1)**t * a_t * p[t]
                    if pos_final < 0 or pos_final > s:
                        return False
                    if pos_final == s:
                        return True
                    return False
                
                if (-1)**segment == 1:
                    min_strokes = max(1, (s - pos - sum(p[segment+1:t]) - p[t]) // p[segment])
                    max_strokes = (s - pos) // p[segment] + 2
                else:
                    min_strokes = 1
                    max_strokes = pos // p[segment] + 2
                for strokes in range(min_strokes, max_strokes):
                    a[segment] = strokes
                    new_pos = pos + (-1)**segment * strokes * p[segment]
                    if new_pos < 0 or new_pos > s:
                        continue
                    new_dist = dist + (-1)**segment * strokes * p[segment]
                    if try_combinations(segment + 1, new_pos, new_dist, positions + [new_pos], a):
                        return True
                return False
            
            a = [1] * t
            if try_combinations(0, 0, 0, [0], a):
                print(final_power)
                return
            continue
        
        a_t = (s - dist) / ((-1)**t * p[t])
        if a_t != int(a_t) or a_t < 1:
            def try_combinations(segment, pos, dist, positions, a):
                if segment == t:
                    a_t = (s - dist) / ((-1)**t * p[t])
                    if a_t != int(a_t) or a_t < 1:
                        return False
                    a_t = int(a_t)
                    pos_final = pos + (-1)**t * a_t * p[t]
                    if pos_final < 0 or pos_final > s:
                        return False
                    if pos_final == s:
                        return True
                    return False
                
                if (-1)**segment == 1:
                    min_strokes = max(1, (s - pos - sum(p[segment+1:t]) - p[t]) // p[segment])
                    max_strokes = (s - pos) // p[segment] + 2
                else:
                    min_strokes = 1
                    max_strokes = pos // p[segment] + 2
                for strokes in range(min_strokes, max_strokes):
                    a[segment] = strokes
                    new_pos = pos + (-1)**segment * strokes * p[segment]
                    if new_pos < 0 or new_pos > s:
                        continue
                    new_dist = dist + (-1)**segment * strokes * p[segment]
                    if try_combinations(segment + 1, new_pos, new_dist, positions + [new_pos], a):
                        return True
                return False
            
            a = [1] * t
            if try_combinations(0, 0, 0, [0], a):
                print(final_power)
                return
            continue
        
        a_t = int(a_t)
        pos_final = pos + (-1)**t * a_t * p[t]
        if pos_final < 0 or pos_final > s:
            continue
        if pos_final == s:
            print(final_power)
            return
    
    print(1)

t = int(input())
for _ in range(t):
    solve()
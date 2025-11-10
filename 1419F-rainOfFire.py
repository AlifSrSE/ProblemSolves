# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[2*i+1])
        y = int(data[2*i+2])
        points.append((x, y))
    
    if n == 1:
        print(0)
        return
    
    def manhattan(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    
    def check(t):
        candidates = set()
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                if d > 2*t:
                    return False
                if d > t:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    if x1 == x2:
                        mid_y = (y1 + y2) // 2
                        candidates.add((x1, mid_y))
                        candidates.add((x1, mid_y+1))
                        candidates.add((x1, mid_y-1))
                    elif y1 == y2:
                        mid_x = (x1 + x2) // 2
                        candidates.add((mid_x, y1))
                        candidates.add((mid_x+1, y1))
                        candidates.add((mid_x-1, y1))
                    else:
                        dx = x2 - x1
                        dy = y2 - y1
                        if abs(dx) >= abs(dy):
                            mid_x = (x1 + x2) // 2
                            y_from_x1 = y1 + (mid_x - x1) * dy // dx
                            candidates.add((mid_x, y_from_x1))
                            candidates.add((mid_x+1, y_from_x1))
                            candidates.add((mid_x-1, y_from_x1))
                        else:
                            mid_y = (y1 + y2) // 2
                            x_from_y1 = x1 + (mid_y - y1) * dx // dy
                            candidates.add((x_from_y1, mid_y))
                            candidates.add((x_from_y1+1, mid_y))
                            candidates.add((x_from_y1-1, mid_y))
        
        candidates.add((0,0))
        for i in range(n):
            candidates.add(points[i])
            candidates.add((points[i][0]+1, points[i][1]))
            candidates.add((points[i][0]-1, points[i][1]))
            candidates.add((points[i][0], points[i][1]+1))
            candidates.add((points[i][0], points[i][1]-1))
        
        for cand in candidates:
            valid = True
            for i in range(n):
                d = manhattan(cand, points[i])
                if d > t:
                    valid = False
                    break
            if valid:
                return True
        return False
    
    left, right = 0, 10**10
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    if left > 10**9:
        print(-1)
    else:
        print(left)

if __name__ == "__main__":
    main()
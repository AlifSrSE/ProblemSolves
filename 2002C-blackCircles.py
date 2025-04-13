# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        points = []
        for _ in range(n):
            points.append((int(input[ptr]), int(input[ptr+1])))
            ptr += 2
        
        xs, ys = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        xt, yt = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        
        target_dist = (xs - xt)**2 + (ys - yt)**2
        all_farther = True
        
        for px, py in points:
            if (px - xt)**2 + (py - yt)**2 <= target_dist:
                all_farther = False
                break
        
        results.append("YES" if all_farther else "NO")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
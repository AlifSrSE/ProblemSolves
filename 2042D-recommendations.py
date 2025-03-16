# Author : AlifSrSE
# Date : 2025-03-03
# Problem link : https://codeforces.com/contest/2042/problem/D

import sys

def find_strongly_recommended_tracks(test_cases):
    results = []
    
    for n, segments in test_cases:
        recommended_counts = [0] * n
        
        for i in range(n):
            li, ri = segments[i]
            min_r = float('inf')
            max_l = -float('inf')
            predictor_count = 0
            
            for j in range(n):
                if i != j:
                    lj, rj = segments[j]
                    if lj <= li and ri <= rj:
                        max_l = max(max_l, lj)
                        min_r = min(min_r, rj)
                        predictor_count += 1
            
            if predictor_count == 0:
                continue
            
            if max_l <= min_r:
                recommended_counts[i] = max(0, min_r - max_l + 1 - (ri - li + 1))
        
        results.append(recommended_counts)
    
    return results

def main():
    t = int(sys.stdin.readline())
    test_cases = []
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        segments = []
        for _ in range(n):
            l, r = map(int, sys.stdin.readline().split())
            segments.append((l, r))
        test_cases.append((n, segments))
    
    results = find_strongly_recommended_tracks(test_cases)
    
    output = sys.stdout.write
    for result in results:
        output('\n'.join(map(str, result)) + '\n')

if __name__ == "__main__":
    main()
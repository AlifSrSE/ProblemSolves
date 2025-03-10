# Author : AlifSrSE
# Date : 2025-03-03
# Problem link : https://codeforces.com/contest/2042/problem/D

import sys
input = sys.stdin.readline

def find_strongly_recommended_tracks(t, test_cases):
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
                recommended_counts[i] = 0
                continue
            
            if max_l <= min_r:
                segment_length = ri - li + 1
                intersection_length = min_r - max_l + 1
                recommended_counts[i] = intersection_length - segment_length if intersection_length > segment_length else 0
            else:
                recommended_counts[i] = 0
        
        results.append(recommended_counts)
    
    return results

def main():
    t = int(input().strip())
    test_cases = []
    
    for _ in range(t):
        n = int(input().strip())
        segments = []
        for _ in range(n):
            l, r = map(int, input().strip().split())
            segments.append((l, r))
        test_cases.append((n, segments))
    
    results = find_strongly_recommended_tracks(t, test_cases)
    
    for result in results:
        for count in result:
            print(count)

if __name__ == "__main__":
    main()
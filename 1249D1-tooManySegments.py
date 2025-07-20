# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1249/problem/D1

import sys
import collections
import heapq

def alif():
    N_MAX = 2 * 10**5 + 7 
    n, k = map(int, sys.stdin.readline().split())
    a = [0] * N_MAX
    s = collections.defaultdict(list) 
    t = collections.defaultdict(list)

    for p in range(n):
        left, right = map(int, sys.stdin.readline().split())
        a[left] += 1
        a[right + 1] -= 1
        s[left].append((right + 1, p + 1))
        t[right + 1].append(p + 1)

    rem = []
    active_intervals_heap = []
    interval_is_removed = set() 

    for p in range(N_MAX):
        for interval_id_to_remove in t[p]:
            interval_is_removed.add(interval_id_to_remove)

        for end_plus_1, interval_id_to_add in s[p]:
            if interval_id_to_add not in interval_is_removed:
                heapq.heappush(active_intervals_heap, (-end_plus_1, interval_id_to_add))
        
        while active_intervals_heap and active_intervals_heap[0][1] in interval_is_removed:
            heapq.heappop(active_intervals_heap)
            
        while len(active_intervals_heap) > k:
            removed_end_plus_1, removed_id = heapq.heappop(active_intervals_heap)
            rem.append(removed_id)
            interval_is_removed.add(removed_id)
            a[-removed_end_plus_1] += 1 

            while active_intervals_heap and active_intervals_heap[0][1] in interval_is_removed:
                heapq.heappop(active_intervals_heap)

    sys.stdout.write(f"{len(rem)}\n")
    sys.stdout.write(" ".join(map(str, rem)) + "\n")

if __name__ == "__main__":
    alif()
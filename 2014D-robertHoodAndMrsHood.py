# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import heapq

def solve(n, d, l, r):
    sorted_indices = sorted(range(len(l)), key=lambda i: l[i])
    overlap_nums = [0] * (n - d + 1)
    rights = []
    index = -1
    while index != len(sorted_indices) - 1 and l[sorted_indices[index + 1]] - 1 <= d - 1:
        heapq.heappush(rights, r[sorted_indices[index + 1]] - 1)
        index += 1
    for i in range(len(overlap_nums)):
        while rights and rights[0] == i - 1:
            heapq.heappop(rights)
        while index != len(sorted_indices) - 1 and l[sorted_indices[index + 1]] - 1 == i + d - 1:
            heapq.heappush(rights, r[sorted_indices[index + 1]] - 1)
            index += 1
        overlap_nums[i] = len(rights)
    min_overlap_num = min(overlap_nums)
    max_overlap_num = max(overlap_nums)
    max_overlap_index = overlap_nums.index(max_overlap_num) + 1
    min_overlap_index = overlap_nums.index(min_overlap_num) + 1
    return f"{max_overlap_index} {min_overlap_index}"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, d, k = map(int, input().split())
        l = [0] * k
        r = [0] * k
        for i in range(k):
            l[i], r[i] = map(int, input().split())
        print(solve(n, d, l, r))
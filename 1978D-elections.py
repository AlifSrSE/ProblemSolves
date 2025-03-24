# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1978/D
 
def solve():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    rest_to_count = {}
    for ai in a:
        rest_to_count[ai] = rest_to_count.get(ai, 0) + 1

    excluded_to_count = {}
    excluded_sum = 0

    prefix_sum = c

    while rest_to_count and prefix_sum + excluded_sum < max(rest_to_count.keys()):
        max_vote = max(rest_to_count.keys())
        rest_to_count[max_vote] -= 1
        if rest_to_count[max_vote] == 0:
            del rest_to_count[max_vote]

        excluded_to_count[max_vote] = excluded_to_count.get(max_vote, 0) + 1
        excluded_sum += max_vote

    result = [0] * n
    for i in range(n):
        prefix_sum += a[i]

        if a[i] in rest_to_count:
            rest_to_count[a[i]] -= 1
            if rest_to_count[a[i]] == 0:
                del rest_to_count[a[i]]
        else:
            excluded_to_count[a[i]] -= 1
            if excluded_to_count[a[i]] == 0:
                del excluded_to_count[a[i]]
            excluded_sum -= a[i]

        while excluded_to_count and prefix_sum + (excluded_sum - min(excluded_to_count.keys())) >= max(rest_to_count.keys(), default=-1):
            vote = min(excluded_to_count.keys())
            excluded_to_count[vote] -= 1
            if excluded_to_count[vote] == 0:
                del excluded_to_count[vote]
            excluded_sum -= vote

            rest_to_count[vote] = rest_to_count.get(vote, 0) + 1

        result[i] = i + len(excluded_to_count)

    winner = 0
    max_vote = a[0] + c
    for i in range(1, n):
        if a[i] > max_vote:
            winner = i
            max_vote = a[i]
    result[winner] = 0

    return ' '.join(map(str, result))

t = int(input())
for _ in range(t):
    print(solve())
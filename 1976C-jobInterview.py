# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1976/C
 
def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    programmer_indices = [i for i in range(len(a)) if a[i] > b[i]]
    programmer_prefix_sums = [0]
    for i in programmer_indices:
        programmer_prefix_sums.append(programmer_prefix_sums[-1] + a[i])

    tester_indices = [i for i in range(len(a)) if a[i] < b[i]]
    tester_prefix_sums = [0]
    for i in tester_indices:
        tester_prefix_sums.append(tester_prefix_sums[-1] + b[i])

    a_suffix_sums = [0]
    for i in range(1, len(a) + 1):
        a_suffix_sums.append(a_suffix_sums[-1] + a[len(a) - i])

    b_suffix_sums = [0]
    for i in range(1, len(b) + 1):
        b_suffix_sums.append(b_suffix_sums[-1] + b[len(b) - i])

    def compute_team_skill(index):
        programmer_or_tester = a[index] > b[index]

        length = -1
        lower = 0
        upper = n + m + 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if compute_num(programmer_indices, index if programmer_or_tester else float('inf'), middle) >= n or \
               compute_num(tester_indices, index if not programmer_or_tester else float('inf'), middle) >= m:
                length = middle
                upper = middle - 1
            else:
                lower = middle + 1

        programmer_num = compute_num(programmer_indices, index if programmer_or_tester else float('inf'), length)
        tester_num = compute_num(tester_indices, index if not programmer_or_tester else float('inf'), length)

        result = 0
        if index < length:
            if programmer_or_tester:
                result += (programmer_prefix_sums[programmer_num + 1] - a[index]) + tester_prefix_sums[tester_num]
            else:
                result += programmer_prefix_sums[programmer_num] + (tester_prefix_sums[tester_num + 1] - b[index])
        else:
            result += programmer_prefix_sums[programmer_num] + tester_prefix_sums[tester_num]

        if programmer_num == n:
            result += b_suffix_sums[n + m + 1 - length] - (b[index] if index >= length else 0)
        else:
            result += a_suffix_sums[n + m + 1 - length] - (a[index] if index >= length else 0)

        return result

    def compute_num(indices, excluded, size):
        index = -1
        for i, val in enumerate(indices):
            if val <= size - 1:
                index = i
            else:
                break
        if index == -1:
            return 0

        result = index + 1
        if index >= 0 and excluded <= indices[index]:
            result -= 1

        return result

    return ' '.join(map(str, [compute_team_skill(i) for i in range(len(a))]))

t = int(input())
for _ in range(t):
    print(solve())
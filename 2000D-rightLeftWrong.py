# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, s):
    n = len(a)
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + a[i - 1]

    result = 0
    left_index = -1
    right_index = n

    while True:
        while left_index != n:
            left_index += 1
            if left_index == n or s[left_index] != 'R':
                break

        while right_index != -1:
            right_index -= 1
            if right_index == -1 or s[right_index] != 'L':
                break

        if left_index > right_index:
            break

        result += prefix_sums[right_index + 1] - prefix_sums[left_index]

    return result

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input().strip()
    print(solve(a, s))

# Author : AlifSrSE
# Date : 2025-02-16
# Link : https://codeforces.com/contest/1085/problem/A

def solve(t):
    left_index = 0
    right_index = len(t) - 1
    left_or_right = len(t) % 2 != 0
    result = []

    for _ in range(len(t)):
        if left_or_right:
            result.append(t[left_index])
            left_index += 1
        else:
            result.append(t[right_index])
            right_index -= 1
        left_or_right = not left_or_right

    return ''.join(reversed(result))


if __name__ == "__main__":
    t = input()
    print(solve(t))

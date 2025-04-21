# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# https://codeforces.com/problemset/problem/2096/E

def solve():
    n = int(input())
    s = input()

    def is_beautiful(arr):
        first_pink = -1
        for i in range(len(arr)):
            if arr[i] == 'P':
                first_pink = i
                break
        if first_pink == -1:
            return True
        for i in range(first_pink + 1, len(arr)):
            if arr[i] == 'B':
                return False
        return True

    if is_beautiful(list(s)):
        print(0)
        return

    q = [(list(s), 0)]
    visited = {"".join(list(s))}

    while q:
        current_arrangement, steps = q.pop(0)

        for i in range(n - 2):
            segment = current_arrangement[i:i+3]
            sorted_segment = sorted(segment)
            next_arrangement = current_arrangement[:i] + sorted_segment + current_arrangement[i+3:]
            next_arrangement_str = "".join(next_arrangement)

            if next_arrangement_str not in visited:
                if is_beautiful(next_arrangement):
                    print(steps + 1)
                    return
                visited.add(next_arrangement_str)
                q.append((next_arrangement, steps + 1))

t = int(input())
for _ in range(t):
    solve()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import deque
import sys

input = sys.stdin.read

def solve_good_permutation(t, test_cases):
    results = []

    for case in test_cases:
        n, a, c = case
        pos_in_a = [0] * (n + 1)
        for i in range(n):
            pos_in_a[a[i]] = i

        b = [0] * n
        used = set()
        fixed = []

        for i in range(n):
            if c[i] != 0:
                b[i] = c[i]
                used.add(c[i])
                fixed.append((i, c[i]))

        missing = deque()
        for i in range(1, n + 1):
            if i not in used:
                missing.append(i)

        for i in range(n):
            if b[i] == 0:
                b[i] = missing.popleft()

        ok = True
        a_copy = a[:]
        
        for i in range(n):
            if a_copy[i] == b[i]:
                continue

            found = False
            for r in range(i + 1, n):
                segment = a_copy[i:r+1]
                if min(segment) == a_copy[r] and a_copy[r] == b[i]:
                    a_copy[i:r+1] = [a_copy[r]] + a_copy[i:r]
                    found = True
                    break

            if not found:
                ok = False
                break

        if ok:
            results.append(" ".join(map(str, b)))
        else:
            results.append("-1")

    return results

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1

    test_cases = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        c = list(map(int, data[idx:idx + n]))
        idx += n
        test_cases.append((n, a, c))

    results = solve_good_permutation(t, test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()

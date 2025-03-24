# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/2034/D

def solve(a):
    index_sets = [set() for _ in range(3)]
    for i, x in enumerate(a):
        index_sets[x].add(i)

    sorted_a = sorted(a)

    moves = []
    for i in range(len(a)):
        while a[i] != sorted_a[i]:
            index = max(index_sets[a[i] - 1])
            moves.append(f"{i + 1} {index + 1}")

            index_sets[a[i]].remove(i)
            index_sets[a[i] - 1].add(i)

            index_sets[a[i] - 1].remove(index)
            index_sets[a[i]].add(index)

            a[i] -= 1
            a[index] += 1

    return f"{len(moves)}\n" + "\n".join(moves)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
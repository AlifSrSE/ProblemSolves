# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1997/D

import threading

def solve(a, p):
    n = len(a)

    child_lists = [[] for _ in range(n)]
    for i, parent in enumerate(p):
        child_lists[parent - 1].append(i + 1)

    def search(node):
        if not child_lists[node]:
            return a[node]

        min_sub = min(search(child) for child in child_lists[node])

        return (a[node] + min_sub) // 2 if a[node] < min_sub else min_sub

    if not child_lists[0]:
        return a[0]
    else:
        return a[0] + min(search(node) for node in child_lists[0])

def main():
    sc = int(input())
    for _ in range(sc):
        n = int(input())
        a = list(map(int, input().split()))
        p = list(map(int, input().split()))
        print(solve(a, p))

if __name__ == "__main__":
    threading.stack_size(1 << 28)
    threading.Thread(target=main).start()
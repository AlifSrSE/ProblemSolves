# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1176/problem/C

from collections import deque

SEQUENCE = [4, 8, 15, 16, 23, 42]

def alif(a):
    index_queues = [deque() for _ in range(len(SEQUENCE))]

    for i, val in enumerate(a):
        for j, seq_val in enumerate(SEQUENCE):
            if seq_val == val:
                index_queues[j].append(i)
                break

    subsequence_num = 0
    while True:
        found = True
        min_index = -1

        for i in range(len(SEQUENCE)):
            while index_queues[i] and index_queues[i][0] <= min_index:
                index_queues[i].popleft()

            if not index_queues[i]:
                found = False
                break

            min_index = index_queues[i].popleft()

        if not found:
            break

        subsequence_num += 1

    return len(a) - subsequence_num * len(SEQUENCE)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(alif(a))

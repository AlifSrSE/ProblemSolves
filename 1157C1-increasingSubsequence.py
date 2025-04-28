# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1156/problem/C1

from collections import deque

def alif(a):
    sequence = deque(a)
    moves = []
    prev = -1

    while sequence and (sequence[0] > prev or sequence[-1] > prev):
        if sequence[0] > prev and (len(sequence) == 1 or sequence[0] < sequence[-1] or sequence[-1] <= prev):
            prev = sequence.popleft()
            moves.append('L')
        elif sequence[-1] > prev:
            prev = sequence.pop()
            moves.append('R')
        else:
            break

    return f"{len(moves)}\n{''.join(moves)}"

if __name__ == "__main__":
    sc = int(input())
    a = list(map(int, input().split()))
    print(alif(a))
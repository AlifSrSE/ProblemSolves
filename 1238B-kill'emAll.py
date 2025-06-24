# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1238/problem/B

from collections import deque
def alif(x, r):
    deque_x = deque(sorted(x))

    left = 0
    result = 0

    while deque_x:
        left += r
        max_val = deque_x.pop() 
        while deque_x and deque_x[-1] == max_val:
            deque_x.pop()
        while deque_x and deque_x[0] <= left:
            deque_x.popleft()
        result += 1
    return result

def _():
    q = int(input())
    for _ in range(q):
        n, r = map(int, input().split())
        x = list(map(int, input().split()))
        print(alif(x, r))

if __name__ == "__main__":
    _()
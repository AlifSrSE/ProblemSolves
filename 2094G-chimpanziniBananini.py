# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import threading
import random

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

class Node:
    __slots__ = ('val', 'prio', 'size', 'sum', 'weighted_sum', 'rev', 'left', 'right')
    def __init__(self, val):
        self.val = val
        self.prio = random.randint(1, 1 << 30)
        self.size = 1
        self.sum = val
        self.weighted_sum = val
        self.rev = False
        self.left = None
        self.right = None

def get_size(t):
    return t.size if t else 0

def get_sum(t):
    return t.sum if t else 0

def get_weighted_sum(t):
    return t.weighted_sum if t else 0

def recalc(t):
    if not t:
        return
    l, r = t.left, t.right
    L = get_size(l)
    t.size = 1 + get_size(l) + get_size(r)
    t.sum = get_sum(l) + t.val + get_sum(r)
    wl = get_weighted_sum(l)
    wr = get_weighted_sum(r)
    sr = get_sum(r)
    t.weighted_sum = wl + t.val * (L + 1) + wr + sr * (L + 1)

def push(t):
    if t and t.rev:
        t.left, t.right = t.right, t.left
        if t.left:
            t.left.rev ^= True
            t.left.weighted_sum = (get_size(t.left) + 1) * t.left.sum - t.left.weighted_sum
        if t.right:
            t.right.rev ^= True
            t.right.weighted_sum = (get_size(t.right) + 1) * t.right.sum - t.right.weighted_sum
        t.rev = False

def split(t, k):
    if not t:
        return None, None
    push(t)
    if get_size(t.left) >= k:
        left, t.left = split(t.left, k)
        recalc(t)
        return left, t
    else:
        t.right, right = split(t.right, k - get_size(t.left) - 1)
        recalc(t)
        return t, right

def merge(a, b):
    if not a or not b:
        return a or b
    push(a)
    push(b)
    if a.prio > b.prio:
        a.right = merge(a.right, b)
        recalc(a)
        return a
    else:
        b.left = merge(a, b.left)
        recalc(b)
        return b

def solve():
    t = int(input())
    for _ in range(t):
        q = int(input())
        root = None
        results = []
        for _ in range(q):
            parts = input().split()
            if parts[0] == '1':
                if get_size(root) > 1:
                    left, right = split(root, get_size(root) - 1)
                    root = merge(right, left)
            elif parts[0] == '2':
                if root:
                    root.rev ^= True
                    root.weighted_sum = (get_size(root) + 1) * root.sum - root.weighted_sum
            else:
                k = int(parts[1])
                root = merge(root, Node(k))
            results.append(str(get_weighted_sum(root)) if root else '0')
        sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    threading.Thread(target=solve).start()

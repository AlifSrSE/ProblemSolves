# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import random

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

MOD = int(1e9 + 7)
N = 1 << 20

class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.size = 1
        self.weight = val
        self.key = random.getrandbits(64)
        self.fi = 0
        self.ad = 0
        self.left_val = val
        self.right_val = val

def update(x):
    if not x:
        return
    x.size = 1 + (x.left.size if x.left else 0) + (x.right.size if x.right else 0)
    x.left_val = x.left.left_val if x.left else x.weight
    x.right_val = x.right.right_val if x.right else x.weight

def add(x, l, h):
    if not x:
        return
    left_size = x.left.size if x.left else 0
    x.weight += l + h * left_size
    x.fi += l
    x.ad += h
    x.left_val += l
    x.right_val += l + h * (x.size - 1)

def push(x):
    if not x or (x.fi == 0 and x.ad == 0):
        return
    if x.left:
        add(x.left, x.fi, x.ad)
    if x.right:
        left_size = x.left.size if x.left else 0
        add(x.right, x.fi + x.ad * (left_size + 1), x.ad)
    x.fi = x.ad = 0

def split(root, t):
    if not root:
        return None, None
    push(root)
    left_size = root.left.size if root.left else 0
    if root.weight <= 0:
        x, root.left = split(root.left, t)
        update(root)
        return x, root
    else:
        root.right, y = split(root.right, t - left_size - 1)
        update(root)
        return root, y

def merge(x, y):
    if not x or not y:
        return x or y
    if x.key < y.key:
        push(x)
        x.right = merge(x.right, y)
        update(x)
        return x
    else:
        push(y)
        y.left = merge(x, y.left)
        update(y)
        return y

def dfs(x, cnt, ns):
    if not x:
        return cnt, ns
    push(x)
    cnt, ns = dfs(x.left, cnt, ns)
    if cnt > 0:
        ns += x.weight
        cnt -= 1
    cnt, ns = dfs(x.right, cnt, ns)
    update(x)
    return cnt, ns

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ia = [0] * (n + 1)
    for i in range(n):
        if a[i]:
            ia[a[i]] = i + 1

    s0 = n // 2
    s1 = (n + 1) // 2
    cnt0 = cnt1 = num = 0
    root = None
    ND = 0

    for i in range(n - 1, -1, -1):
        if ia[i + 1]:
            if ia[i + 1] % 2 == 0:
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            num += 1
            ls, rs = split(root, 0)
            root = merge(merge(ls, Node(0)), rs)

        ND += (num + cnt0 + cnt1) * (num + cnt0 + cnt1 + 1) // 2
        ND += cnt0 * (s0 - cnt0)
        ND += (num + cnt1) * (s1 - num - cnt1)

        add(root, (s0 - 2 * cnt0) + (2 * num + 2 * cnt1 - s1) - 2, -4)

    ns = 0
    cnt = s0 - cnt0
    _, ns = dfs(root, cnt, ns)

    print(ND + ns)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

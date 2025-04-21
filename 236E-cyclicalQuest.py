# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/236/problem/E

import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    maxn = 2 * n + 5
    kinds = 26

    go = [[0] * kinds for _ in range(maxn)]
    slink = [0] * maxn
    length = [0] * maxn
    cnt = [0] * maxn
    cc = [0] * maxn
    per = [0] * maxn

    size = 2
    last = 1
    length[0] = -1
    go[0] = [1] * kinds

    def extend(c_int):
        nonlocal size, last
        p = last
        while not go[p][c_int]:
            go[p][c_int] = size
            p = slink[p]

        q = go[p][c_int]
        length[size] = length[last] + 1
        cnt[size] = 1
        last = size
        size += 1

        if not p:
            slink[last] = 1
        elif length[p] + 1 == length[q]:
            slink[last] = q
        else:
            new_node = size
            length[new_node] = length[p] + 1
            go[new_node] = list(go[q])
            slink[new_node] = slink[q]
            while go[p][c_int] == q:
                go[p][c_int] = new_node
                p = slink[p]
            slink[last] = new_node
            slink[q] = new_node
            size += 1

    def build():
        for char in s:
            extend(ord(char) - ord('a'))

    def build_match():
        for i in range(size):
            per[i] = i

        per.sort(key=lambda i: length[i], reverse=True)

        for st in per[:size]:
            cnt[slink[st]] += cnt[st]

    tc = 0

    def lcs(t_str):
        nonlocal tc
        tc += 1
        l_t = len(t_str)
        doubled_t = t_str + t_str[:-1]
        current_state = 1
        current_len = 0
        total_sum = 0

        for char in doubled_t:
            c_int = ord(char) - ord('a')
            while current_state > 0 and not go[current_state][c_int]:
                current_state = slink[current_state]
                if current_state > 0:
                    current_len = length[current_state]
                else:
                    current_len = 0
                    break

            if go[current_state][c_int]:
                current_state = go[current_state][c_int]
                current_len += 1
            else:
                current_state = 1
                current_len = 0

            if current_len >= l_t:
                while True:
                    sl = slink[current_state]
                    if length[sl] >= l_t:
                        current_state = sl
                    else:
                        break

                if cc[current_state] != tc:
                    total_sum += cnt[current_state]
                    cc[current_state] = tc
        return total_sum

    build()
    build_match()

    q = int(sys.stdin.readline())
    for _ in range(q):
        t = sys.stdin.readline().strip()
        result = lcs(t)
        print(result)

if __name__ == "__main__":
    solve()
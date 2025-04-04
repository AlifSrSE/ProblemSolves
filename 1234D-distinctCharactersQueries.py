# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    s = input()
    t = int(input())
    n = len(s)
    s = "#" + s

    tree = [[0] * (4 * n) for _ in range(26)]

    def build_tree(nd, l, r, id):
        if l == r:
            val = ord(s[l]) - ord('a')
            if val == id:
                tree[id][nd] = 1
            return

        left = 2 * nd
        right = 2 * nd + 1
        mid = (l + r) // 2
        build_tree(left, l, mid, id)
        build_tree(right, mid + 1, r, id)

        tree[id][nd] = tree[id][left] + tree[id][right]

    def update(nd, l, r, pos, id, type_val):
        if l > pos or r < pos:
            return
        if l == r and l == pos:
            if type_val == 1:
                tree[id][nd] = 1
            else:
                tree[id][nd] = 0
            return

        left = nd * 2
        right = nd * 2 + 1
        mid = (l + r) // 2
        update(left, l, mid, pos, id, type_val)
        update(right, mid + 1, r, pos, id, type_val)

        tree[id][nd] = tree[id][left] + tree[id][right]

    def query(nd, l, r, x, y, id):
        if y < l or x > r:
            return 0
        if l >= x and r <= y:
            return tree[id][nd]

        left = nd * 2
        right = nd * 2 + 1
        mid = (l + r) // 2
        p = query(left, l, mid, x, y, id)
        q = query(right, mid + 1, r, x, y, id)
        return p + q

    for i in range(26):
        build_tree(1, 1, n - 1, i)

    for _ in range(t):
        x, *args = map(str, input().split())
        x = int(x)

        if x == 1:
            pos, c = int(args[0]), args[1]

            if s[pos] == c:
                continue
            new_id = ord(c) - ord('a')

            update(1, 1, n - 1, pos, ord(s[pos]) - ord('a'), 2)
            s = s[:pos] + c + s[pos + 1:]
            update(1, 1, n - 1, pos, new_id, 1)

        else:
            l, r = int(args[0]), int(args[1])
            cnt = 0

            for i in range(26):
                tmp = query(1, 1, n - 1, l, r, i)
                if tmp:
                    cnt += 1
            print(cnt)

solve()
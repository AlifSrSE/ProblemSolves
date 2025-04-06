# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1

    results = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        a = [int(data[i]) - 1 for i in range(idx, idx + n)]
        idx += n

        size = n
        tree = [0] * (2 * size)
        prefix = [0] * size
        ans = [0] * size

        def update(p, v):
            p += size
            tree[p] = max(tree[p], v)
            while p > 1:
                p >>= 1
                tree[p] = max(tree[2 * p], tree[2 * p + 1])

        def query(l, r):
            res = 0
            l += size
            r += size
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l >>= 1
                r >>= 1
            return res

        prefix[0] = a[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], a[i])

        for i in range(n - 1, -1, -1):
            ans[i] = max(prefix[i], query(0, prefix[i]))
            update(a[i], ans[i])

        results.append(' '.join(str(x + 1) for x in ans))

    print('\n'.join(results))


if __name__ == "__main__":
    main()

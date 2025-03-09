def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        a = input()
        b = input()
        
        va = [[0] * 26 for _ in range(n + 1)]
        vb = [[0] * 26 for _ in range(n + 1)]
        
        for p in range(n):
            for u in range(26):
                va[p + 1][u] = va[p][u]
            va[p + 1][ord(a[p]) - ord('a')] += 1
        
        for p in range(n):
            for u in range(26):
                vb[p + 1][u] = vb[p][u]
            vb[p + 1][ord(b[p]) - ord('a')] += 1
        
        for _ in range(q):
            left, right = map(int, input().split())
            total = 0
            
            for p in range(26):
                ca = va[right][p] - va[left - 1][p]
                cb = vb[right][p] - vb[left - 1][p]
                diff = cb - ca
                if diff < 0:
                    diff = -diff
                total += diff
            
            print(total // 2)

if __name__ == "__main__":
    main()
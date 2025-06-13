# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1207/problem/B

def alif():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    R_OFFSETS = [-1, -1, 0, 0]
    C_OFFSETS = [-1, 0, -1, 0]
    operations = set()

    for r in range(n):
        for c in range(m):
            if A[r][c] == 1:
                found = False
                for i in range(len(R_OFFSETS)):
                    x = r + R_OFFSETS[i]
                    y = c + C_OFFSETS[i]
                    if (x >= 0 and x < n and y >= 0 and y < m and
                        all(0 <= x - R_OFFSETS[j] < n and 0 <= y - C_OFFSETS[j] < m and
                            A[x - R_OFFSETS[j]][y - C_OFFSETS[j]] == 1
                            for j in range(len(R_OFFSETS)))):
                        operations.add(f"{x + 1} {y + 1}")
                        found = True
                        break
                if not found:
                    print(-1)
                    return
    print(len(operations))
    for op in operations:
        print(op)

if __name__ == "__main__":
    alif()
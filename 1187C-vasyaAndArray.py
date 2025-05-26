# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1187/problem/C

def alif():
    n, m = map(int, input().split())

    queries = []
    for _ in range(m):
        t, l, r = map(int, input().split())
        queries.append(((l - 1, r - 1), t))

    queries.sort()

    must_increase = [False] * (n - 1)

    for (l, r), query_type in queries:
        if query_type == 1:
            for i in range(l, r):
                must_increase[i] = True

    a = [0] * n
    a[0] = n

    for i in range(n - 1):
        if must_increase[i]:
            a[i+1] = a[i] - 1
        else:
            a[i+1] = a[i]

    possible = True
    for (l, r), query_type in queries:
        if query_type == 1:
            for i in range(l, r):
                if a[i] >= a[i+1]:
                    possible = False
                    break
        else:
            for i in range(l, r):
                if a[i] < a[i+1]:
                    possible = False
                    break
        if not possible:
            break

    if possible:
        print("YES")
        print(*(a))
    else:
        print("NO")

if __name__ == "__main__":
    alif()

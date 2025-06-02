# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1198/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    s = [False] * n
    
    q = int(input())
    queries = []
    for _ in range(q):
        query_parts = list(map(int, input().split()))
        queries.append(query_parts)
    dist = 0

    for p in range(q - 1, -1, -1):
        query_type = queries[p][0]
        
        if query_type == 1:
            who = queries[p][1] - 1
            amount = queries[p][2]
            
            if s[who]:
                continue
            
            s[who] = True
            a[who] = max(amount, dist)
        elif query_type == 2:
            dist = max(dist, queries[p][1])

    for p in range(n):
        if not s[p]:
            a[p] = max(a[p], dist)
        print(a[p], end=" ")
    print()

if __name__ == "__main__":
    alif()

# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1196/problem/B

def alif():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        total_sum = 0
        for x in a:
            total_sum += x
        
        res = []
        for p in range(n):
            if len(res) >= k - 1:
                break
            if a[p] % 2 != 0:
                res.append(p + 1)
        
        res.append(n)

        if (k % 2 != total_sum % 2) or (len(res) < k):
            print("NO")
        else:
            print("YES")
            print(*res)

if __name__ == "__main__":
    alif()
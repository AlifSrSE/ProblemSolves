# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1190/problem/A

def alif():
    n, m, k = map(int, input().split())
    v = [0] + list(map(int, input().split()))
    
    ans = 0
    current_sum = 0
    now = 1
    
    while now <= m:
        r = ((v[now] - current_sum - 1) // k + 1) * k + current_sum
        while now <= m and v[now] <= r:
            current_sum += 1
            now += 1 
        ans += 1

    print(ans)

if __name__ == "__main__":
    alif()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n, k, mp, val):
    if k >= 130 or k <= 0 or n == 0:
        return 0
    if n in mp[k]:
        return mp[k][n]
    
    ans = 0
    c = 0
    for i in range(30, -1, -1):
        if val[i] <= n:
            c = val[i]
            break
    
    for i in range(0, n + 1, c):
        if i + c <= n:
            ans += solve(c - 1, k - i // c, mp, val)
        else:
            ans += solve(n % c, k - i // c, mp, val)
        
        if k - i // c == 0:
            ans += 1
    
    mp[k][n] = ans
    return ans


def main():
    val = [0] * 31
    val[0] = 1
    for i in range(1, 31):
        val[i] = val[i - 1] * 4 + 1
    
    T = int(input())
    for _ in range(T):
        l, r, k = map(int, input().split())
        
        mp = [dict() for _ in range(130)]
        
        result = solve(r, k, mp, val) - solve(l - 1, k, mp, val)
        print(result)


if __name__ == "__main__":
    main()

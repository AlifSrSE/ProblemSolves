# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1197/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        if n < 2:
            print(0)
            continue
        
        ma = 0
        mb = 0
        for x in a:
            if x >= ma:
                mb = ma
                ma = x
            elif x > mb:
                mb = x
        
        if mb < 2:
            print(0)
            continue
        
        ans = n - 2
        ans = min(ans, mb - 1)
        
        print(ans)

if __name__ == "__main__":
    alif()
# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1196/problem/D2

def alif():
    templ = "RGB"

    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        mn = float('inf')

        for d in range(3):
            cnt = 0
            for p in range(k):
                if s[p] != templ[(d + p) % 3]:
                    cnt += 1
            mind = cnt
            for p in range(k, n):
                if s[p] != templ[(d + p) % 3]:
                    cnt += 1
                
                if s[p - k] != templ[(d + p - k) % 3]:
                    cnt -= 1
                mind = min(mind, cnt)
            mn = min(mn, mind)
        print(mn)

if __name__ == "__main__":
    alif()
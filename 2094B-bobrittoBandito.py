# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    t = int(input())
    for _ in range(t):
        n, m, l, r = map(int, input().split())
        L = -l
        R = r
        a = min(m, L)
        b = m - a
        print(-a, b)

if __name__ == "__main__":
    main()

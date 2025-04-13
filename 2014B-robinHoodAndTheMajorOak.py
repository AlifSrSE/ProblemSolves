# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n, k):
    return (n * k - k * (k - 1) // 2) % 2 == 0

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print("YES" if solve(n, k) else "NO")
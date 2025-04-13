# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    if len(a) <= 2:
        return -1

    a.sort()
    return max(0, 2 * a[len(a) // 2] * len(a) - sum(a) + 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
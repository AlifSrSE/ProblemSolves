# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    return all(a[i] > max(1, max(i, len(a) - 1 - i) * 2) for i in range(len(a)))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if solve(a) else "NO")

if __name__ == "__main__":
    main()

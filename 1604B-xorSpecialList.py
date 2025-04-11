# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    if len(a) % 2 != 0 and all(a[i] < a[i + 1] for i in range(len(a) - 1)):
        return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if solve(a) else "NO")

if __name__ == "__main__":
    main()

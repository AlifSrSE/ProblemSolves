# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(x, y):
    return y == x + 1 or (y < x and (x - y + 1) % 9 == 0)

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print("YES" if solve(x, y) else "NO")

if __name__ == "__main__":
    main()

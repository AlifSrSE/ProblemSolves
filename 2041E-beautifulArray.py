# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    a, b = map(int, input().split())

    if a == b:
        print(1)
        print(b)
        return

    n = 2
    arr = [b, 2 * a - b]
    print(n)
    print(*arr)

if __name__ == "__main__":
    solve() 
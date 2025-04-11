# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    result = 0
    size = 0
    for ai in a:
        size += 1
        added = max(0, ai - size)
        result += added
        size += added
    return result

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == "__main__":
    main()

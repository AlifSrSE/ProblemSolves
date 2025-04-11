# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s, m):
    result = 0
    for si in s:
        if len(si) > m:
            break
        m -= len(si)
        result += 1
    return result

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = [input().strip() for _ in range(n)]
        print(solve(s, m))

if __name__ == "__main__":
    main()

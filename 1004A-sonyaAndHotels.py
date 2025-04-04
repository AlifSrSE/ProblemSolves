# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(x, d):
    result = sum(min(2, max(0, (x[i] - d) - (x[i - 1] + d) + 1)) for i in range(1, len(x))) + 2
    return result

def main():
    n, d = map(int, input().split())
    x = list(map(int, input().split()))
    print(solve(x, d))

if __name__ == "__main__":
    main()
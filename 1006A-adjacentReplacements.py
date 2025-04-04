# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    return [x - 1 + x % 2 for x in a]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(" ".join(map(str, solve(a))))

if __name__ == "__main__":
    main()
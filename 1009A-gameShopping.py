# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(c, a):
    result = 0
    index_a = 0
    for ci in c:
        if index_a < len(a) and a[index_a] >= ci:
            result += 1
            index_a += 1
    return result

def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(solve(c, a))

if __name__ == "__main__":
    main()
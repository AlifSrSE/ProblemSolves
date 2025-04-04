# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, k):
    result = -1.0
    for i in range(len(a)):
        sum_val = 0
        for j in range(i, len(a)):
            sum_val += a[j]
            if j - i + 1 >= k:
                result = max(result, sum_val / (j - i + 1.0))
    return result

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, k))

if __name__ == "__main__":
    main()
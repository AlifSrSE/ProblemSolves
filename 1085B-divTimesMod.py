# Author : AlifSrSE
# Date : 2025-02-16
# Link : https://codeforces.com/contest/1085/problem/B

def solve(n, k):
    result = float('inf')
    for remainder in range(1, k):
        if n % remainder == 0:
            result = min(result, (n // remainder) * k + remainder)
    return result


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n, k))

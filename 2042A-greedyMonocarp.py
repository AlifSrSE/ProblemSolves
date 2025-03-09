import sys

def solve(a, k):
    sorted_a = sorted(a, reverse=True)
    sum_ = 0
    for num in sorted_a:
        if sum_ + num > k:
            break
        sum_ += num
    return k - sum_

def main():
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, k))

if __name__ == "__main__":
    main()

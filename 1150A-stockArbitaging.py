# Author : AlifSrSE
# Date : 2025-02-16
# Link : https://codeforces.com/contest/1150/problem/A

def main():
    n, m, r = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_a = min(a)
    max_b = max(b)

    if max_b > min_a:
        coins = r // min_a
        r -= coins * min_a
        r += coins * max_b

    print(r)

if __name__ == "__main__":
    main()

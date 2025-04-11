# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n):
    dp = {0}
    for c in n:
        next_dp = set()
        digit = int(c)
        for prev in dp:
            next_dp.add((prev + digit) % 9)
            if digit <= 3:
                next_dp.add((prev + digit * digit) % 9)
        dp = next_dp
    return 0 in dp

def main():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        print("YES" if solve(n) else "NO")

if __name__ == "__main__":
    main()

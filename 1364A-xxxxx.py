import sys

def alif():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    total_sum = sum(a)

    if total_sum % x != 0:
        print(n)
        return
    first_invalid_left = -1

    for i in range(n):
        if a[i] % x != 0:
            first_invalid_left = i
            break

    if first_invalid_left == -1:
        print(-1)
        return
        
    first_invalid_right = -1
    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            first_invalid_right = i
            break
            
    ans = max(n - (first_invalid_left + 1), first_invalid_right)
    print(ans)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
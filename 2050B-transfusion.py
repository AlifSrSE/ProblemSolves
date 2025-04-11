# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    total = sum(a)
    n = len(a)
    if total % n != 0:
        return False

    average = total // n
    even_indices = [i for i in range(n) if i % 2 == 0]
    even_sum = sum(a[i] for i in even_indices)

    return even_sum == average * len(even_indices)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if solve(a) else "NO")

if __name__ == "__main__":
    main()

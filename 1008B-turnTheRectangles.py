# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(w, h):
    prev = float('inf')
    for i in range(len(w)):
        min_val = min(w[i], h[i])
        max_val = max(w[i], h[i])

        if min_val > prev:
            return False

        if max_val <= prev:
            prev = max_val
        else:
            prev = min_val
    return True

def main():
    n = int(input())
    w = []
    h = []
    for _ in range(n):
        wi, hi = map(int, input().split())
        w.append(wi)
        h.append(hi)
    print("YES" if solve(w, h) else "NO")

if __name__ == "__main__":
    main()
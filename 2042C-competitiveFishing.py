import sys

def solve():
    n, k = map(int, input().split())
    s = input().strip()
    
    v, res, sum_ = 0, 1, 0
    a = []
    
    for i in range(n - 1, 0, -1):
        v += 1 if s[i] == '1' else -1
        a.append(v)
    
    a.sort()
    j = n - 2
    
    while j >= 0 and sum_ < k:
        sum_ += a[j]
        j -= 1
        res += 1
    
    print(res if sum_ >= k else -1)

def main():
    t = int(input().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
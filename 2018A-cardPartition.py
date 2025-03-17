# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2018/problem/A
 
def solve(a, k):
    sum_a = sum(a)
    max_a = max(a)

    for i in range(len(a), 0, -1):
        total = (sum_a + k) // i * i
        if total >= sum_a and total <= sum_a + k and total // i >= max_a:
            return i
    return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        a = list(map(int, data[idx + 2:idx + 2 + n]))
        idx += 2 + n
        
        print(solve(a, k))

if __name__ == "__main__":
    main()
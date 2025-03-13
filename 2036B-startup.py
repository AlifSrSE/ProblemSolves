# Author : AlifSrSE
# Date : 2025-03-12
# Problem link : https://codeforces.com/contest/2036/problem/B

def solve(n, b, c):
    brand_to_cost_sum = {}
    for brand, cost in zip(b, c):
        brand_to_cost_sum[brand] = brand_to_cost_sum.get(brand, 0) + cost
    
    return sum(sorted(brand_to_cost_sum.values(), reverse=True)[:n])


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        b = []
        c = []
        for _ in range(k):
            brand, cost = map(int, input().split())
            b.append(brand)
            c.append(cost)
        
        print(solve(n, b, c))


if __name__ == "__main__":
    main()

# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def check_rent(budget, cost, money, count):
    n = len(budget)
    m = len(cost)
    if count > m or count > n:
        return -1

    extra = 0
    budget_sum = 0
    total_cost = 0

    for p in range(count):
        total_cost += cost[p]
        if cost[p] < budget[n - count + p]:
            budget_sum += cost[p]
        else:
            budget_sum += budget[n - count + p]
            extra += cost[p] - budget[n - count + p]

    if extra > money:
        return -1
    if total_cost < money:
        return 0
    return total_cost - money


def main():
    n, m, a = map(int, input().split())

    b = list(map(int, input().split()))
    b.sort()

    c = list(map(int, input().split()))
    c.sort()

    left = 1
    right = min(m, n)
    budget_needed = 0

    while left <= right:
        mid = (left + right) // 2
        budget_needed = check_rent(b, c, a, mid)
        if budget_needed < 0:
            right = mid - 1
        else:
            left = mid + 1

    budget_needed = check_rent(b, c, a, right)
    print(f"{right} {budget_needed}")


if __name__ == "__main__":
    main()

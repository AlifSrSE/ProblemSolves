# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    list_dict = {}
    for _ in range(m):
        fruit = input()
        if fruit in list_dict:
            list_dict[fruit] += 1
        else:
            list_dict[fruit] = 1
    
    counts = list(list_dict.values())
    
    prices.sort()
    counts.sort()
    
    min_sum = 0
    max_sum = 0
    c = len(counts)
    for p in range(c):
        min_sum += counts[p] * prices[c - 1 - p]
        max_sum += counts[p] * prices[n - c + p]
    
    print(f"{min_sum} {max_sum}")

if __name__ == "__main__":
    main()
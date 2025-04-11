# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import defaultdict

def solve(a):
    value_to_count = defaultdict(int)
    for ai in a:
        value_to_count[ai] += 1

    while value_to_count:
        min_value = min(value_to_count.keys())
        if value_to_count[min_value] == 1:
            return False
        if value_to_count[min_value] != 2:
            value_to_count[min_value + 1] += value_to_count[min_value] - 2
        del value_to_count[min_value]

    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())  
        a = list(map(int, input().split()))
        print("YES" if solve(a) else "NO")

if __name__ == "__main__":
    main()

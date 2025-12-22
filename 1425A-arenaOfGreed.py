#Author: AlifSrSE

import sys

def solve(N):
    coins = [0, 0]
    index = 0
    rest = N
    while rest != 0:
        if rest == 4 or rest % 4 == 2:
            coins[index] += rest // 2
            rest //= 2
        else:
            coins[index] += 1
            rest -= 1
        index = 1 - index
    return coins[0]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        N = int(input_data[i])
        results.append(str(solve(N)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
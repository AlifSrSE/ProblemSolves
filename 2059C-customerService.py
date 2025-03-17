# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2059/problem/C
 
def solve(a):
    last_one_counts = sorted(count_last_one(line) for line in a)

    result = 0
    needed = 0
    for last_one_count in last_one_counts:
        if last_one_count >= needed:
            needed += 1
            result += 1

    return result

def count_last_one(line):
    index = len(line)
    while index >= 1 and line[index - 1] == 1:
        index -= 1

    return len(line) - index

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))

        print(solve(a))
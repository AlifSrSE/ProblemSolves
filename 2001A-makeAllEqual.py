# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import defaultdict

def solve(a):
    value_to_count = defaultdict(int)
    for num in a:
        value_to_count[num] += 1
    return len(a) - max(value_to_count.values())

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        print(solve(a))

if __name__ == "__main__":
    main()
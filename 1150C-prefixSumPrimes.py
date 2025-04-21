# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1150/problem/C

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    tiles = list(map(int, data[1:]))
    
    ones = tiles.count(1)
    twos = tiles.count(2)

    result = []

    if twos > 0 and ones > 0:
        result.append(2)
        result.append(1)
        twos -= 1
        ones -= 1

    result.extend([2] * twos)
    result.extend([1] * ones)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

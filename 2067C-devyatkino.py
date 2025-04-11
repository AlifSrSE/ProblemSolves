# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def check(n, operation_num):
    min_diff = 7
    value = n - operation_num
    while value != 0:
        min_diff = min(min_diff, (7 - value % 10) % 10)
        value //= 10
    return min_diff <= operation_num

def solve(n):
    result = 0
    while True:
        if check(n, result):
            return result
        result += 1

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))

if __name__ == "__main__":
    main()

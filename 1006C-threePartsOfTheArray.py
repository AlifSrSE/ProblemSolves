# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(d):
    result = 0
    left_sum = 0
    right_sum = 0
    left_index = -1
    right_index = len(d)
    while left_index + 1 != right_index:
        if left_sum <= right_sum:
            left_index += 1
            left_sum += d[left_index]
        else:
            right_index -= 1
            right_sum += d[right_index]

        if left_sum == right_sum:
            result = max(result, left_sum)
    return result

def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(solve(d))

if __name__ == "__main__":
    main()
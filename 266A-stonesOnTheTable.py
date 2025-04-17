# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/266/A

def solve():
    length = int(input())
    input_str = input()

    total = 0
    index = 1
    if length > 0:
        state = input_str[0]
        while index < length:
            if input_str[index] == state:
                total += 1
            else:
                state = input_str[index]
            index += 1
    print(total)

if __name__ == "__main__":
    solve()
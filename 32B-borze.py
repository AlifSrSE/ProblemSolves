# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/32/B

def solve():
    input_str = input()
    index = 0
    result = ""
    while index < len(input_str):
        if input_str[index] == '.':
            result += "0"
            index += 1
        elif input_str[index] == '-' and index + 1 < len(input_str):
            if input_str[index + 1] == '.':
                result += "1"
                index += 2
            elif input_str[index + 1] == '-':
                result += "2"
                index += 2
            else:
                index += 1
        else:
            index += 1

    print(result)

if __name__ == "__main__":
    solve()
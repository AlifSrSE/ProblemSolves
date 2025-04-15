# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/1/B

def convert_to_numeric(input_str):
    output = 0
    alpha_size = 26
    for k in range(len(input_str)):
        output = alpha_size * output + (ord(input_str[k]) - ord('A') + 1)
    return output

def convert_to_alpha(input_num):
    alpha_size = 26
    output = ""
    while input_num > 0:
        letter = 'Z'
        input_mod = input_num % alpha_size
        if input_mod > 0:
            letter = chr(ord('A') + input_mod - 1)
        else:
            input_num -= alpha_size
        input_num //= alpha_size
        output = letter + output
    return output

def solve():
    n = int(input())
    for _ in range(n):
        line = input()

        coordinates = False
        if line[0] == 'R' and '0' <= line[1] <= '9' and line.find('C') > 1 and line.find('C') < len(line) - 1:
            coordinates = True

        if coordinates:
            c_pos = line.find('C')
            row_string = line[1:c_pos]
            col_string = line[c_pos + 1:]
            col = int(col_string)
            print(convert_to_alpha(col) + row_string)
        else:
            row_string = ""
            col_string = ""
            for k in range(len(line)):
                if '0' <= line[k] <= '9':
                    col_string = line[k:]
                    break
                else:
                    row_string += line[k]
            print("R" + col_string + "C" + str(convert_to_numeric(row_string)))

solve()
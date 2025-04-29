# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/711/problem/A

def alif():
    n = int(input())
    bus = []
    found = False
    found_row_index = -1

    for i in range(n):
        row_str = input()
        bus.append(list(row_str))
        if not found:
            if row_str[0] == 'O' and row_str[1] == 'O':
                bus[i][0] = '+'
                bus[i][1] = '+'
                found = True
                found_row_index = i
            elif row_str[3] == 'O' and row_str[4] == 'O':
                bus[i][3] = '+'
                bus[i][4] = '+'
                found = True
                found_row_index = i

    if found:
        print("YES")
        for row in bus:
            print("".join(row))
    else:
        print("NO")

if __name__ == "__main__":
    alif()
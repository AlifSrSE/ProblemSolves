# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/20/A

def solve():
    path = input()
    output = ""
    flag = False

    for k in range(len(path)):
        if path[k] != '/' or not flag:
            output += path[k]
        if path[k] == '/':
            flag = True
        else:
            flag = False

    if flag and len(output) > 1:
        output = output[:-1]

    print(output)

solve()
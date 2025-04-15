# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/16/A

def solve():
    n, m = map(int, input().split())

    current_color = -1
    output = True

    for row in range(n):
        current_line = input()
        if current_line[0] == current_color or not output:
            output = False
            break
        else:
            current_color = current_line[0]
            for col in range(1, m):
                if current_line[col] != current_color:
                    output = False
                    break
            if not output:
                break

    if output:
        print("YES")
    else:
        print("NO")

solve()
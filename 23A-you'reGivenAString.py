# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/23/A

def solve():
    input_str = input()
    output = 0

    for length in range(len(input_str) - 1, 0, -1):
        if output > 0:
            break
        present = set()

        for start in range(len(input_str) - length + 1):
            current = input_str[start:start + length]
            if current not in present:
                present.add(current)
            else:
                output = length
                break

    print(output)

solve()
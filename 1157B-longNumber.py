# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1156/problem/B

def alif(a, f):
    digits = [int(char) for char in a]
    n = len(digits)

    begin_index = 0
    while begin_index < n and f[digits[begin_index]] <= digits[begin_index]:
        begin_index += 1

    for i in range(begin_index, n):
        if f[digits[i]] >= digits[i]:
            digits[i] = f[digits[i]]
        else:
            break

    return "".join(map(str, digits))

if __name__ == "__main__":
    sc = input()
    a = input()
    f_input = input().split()
    f = [0] * 10
    for i in range(1, 10):
        f[i] = int(f_input[i - 1])

    print(alif(a, f))
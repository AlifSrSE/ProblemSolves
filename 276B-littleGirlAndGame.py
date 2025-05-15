# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/276/B

def solve():
    line = input()
    alpha_length = 26
    array = [0] * alpha_length

    for char in line:
        if 'a' <= char <= 'z':
            array[ord(char) - ord('a')] += 1

    odd_letters = 0
    for count in array:
        if count % 2 != 0:
            odd_letters += 1

    if odd_letters == 0 or odd_letters % 2 == 1:
        print("First")
    else:
        print("Second")

if __name__ == "__main__":
    solve()
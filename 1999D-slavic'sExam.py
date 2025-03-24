# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/D
 
def solve(s, t):
    letters = list(s)
    index = 0
    for c in t:
        while index != len(letters) and (letters[index] != '?' and letters[index] != c):
            index += 1

        if index == len(letters):
            return "NO"

        if letters[index] == '?':
            letters[index] = c

        index += 1

    for i in range(index, len(letters)):
        if letters[i] == '?':
            letters[i] = 'a'

    return "YES\n" + "".join(letters)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input()
        t = input()
        print(solve(s, t))
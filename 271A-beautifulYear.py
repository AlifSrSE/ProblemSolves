# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/271/A

def is_beautiful(year):
    s_year = str(year)
    return len(set(s_year)) == len(s_year)

def solve():
    number = int(input())
    number += 1
    while not is_beautiful(number):
        number += 1
    print(number)

if __name__ == "__main__":
    solve()
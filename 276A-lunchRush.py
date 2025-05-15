# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/276/A

def solve():
    num_places, time_limit = map(int, input().split())
    max_joy = -10**9
    for _ in range(num_places):
        joy, time = map(int, input().split())
        new_joy = joy if time < time_limit else joy - (time - time_limit)
        if new_joy > max_joy:
            max_joy = new_joy
    print(max_joy)

if __name__ == "__main__":
    solve()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/266/B

def solve():
    num_kids, seconds = map(int, input().split())
    q = list(input())

    for _ in range(seconds):
        index = 0
        while index < num_kids - 1:
            if q[index] == 'B' and q[index + 1] == 'G':
                q[index], q[index + 1] = q[index + 1], q[index]
                index += 2
            else:
                index += 1

    print("".join(q))

if __name__ == "__main__":
    solve()
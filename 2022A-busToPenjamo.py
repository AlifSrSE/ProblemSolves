# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, r):
    full_row = sum(ai // 2 for ai in a)
    rest_row = r - full_row
    alone_num = sum(ai % 2 for ai in a)
    return full_row * 2 + (alone_num if alone_num <= rest_row else rest_row * 2 - alone_num)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, r = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, r))
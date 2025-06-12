# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1206/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    neg_count = 0
    zero_count = 0

    for ai in a:
        if ai < 0:
            result += -1 - ai
            neg_count += 1
        elif ai > 0:
            result += ai - 1
        else:
            result += 1
            zero_count += 1

    if zero_count == 0 and neg_count % 2 != 0:
        result += 2
    print(result)

if __name__ == "__main__":
    alif()
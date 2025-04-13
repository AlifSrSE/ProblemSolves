# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, k):
    result = 0
    rest = 0
    for ai in a:
        if ai >= k:
            rest += ai
        elif ai == 0 and rest != 0:
            rest -= 1
            result += 1
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, k))
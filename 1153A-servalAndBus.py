# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1153/problem/A

def divide_to_ceil(x, y):
    if x < 0:
        return 0
    return x // y + (0 if x % y == 0 else 1)

def alif(s, d, t):
    min_time = float('inf')
    result = -1

    for i in range(len(s)):
        time = divide_to_ceil(t - s[i], d[i]) * d[i] + s[i]
        if time < min_time:
            min_time = time
            result = i + 1

    return result

if __name__ == "__main__":
    n, t = map(int, input().split())
    s = []
    d = []
    for _ in range(n):
        si, di = map(int, input().split())
        s.append(si)
        d.append(di)

    print(alif(s, d, t))

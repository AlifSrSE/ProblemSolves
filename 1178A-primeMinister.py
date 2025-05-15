# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1178/problem/A

def alif(a):
    indices = [0]
    for i in range(1, len(a)):
        if a[0] >= a[i] * 2:
            indices.append(i)

    if sum(a[i] for i in indices) * 2 > sum(a):
        return f"{len(indices)}\n{' '.join(map(str, [i + 1 for i in indices]))}"
    else:
        return "0"

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(alif(a))

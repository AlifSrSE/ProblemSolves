# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1154/problem/B

def alif(a):
    sorted_distincts = sorted(set(a))
    if len(sorted_distincts) == 1:
        return 0
    elif len(sorted_distincts) == 2:
        diff = sorted_distincts[1] - sorted_distincts[0]
        return diff // 2 if diff % 2 == 0 else diff
    elif len(sorted_distincts) == 3:
        diff0 = sorted_distincts[1] - sorted_distincts[0]
        diff1 = sorted_distincts[2] - sorted_distincts[1]
        if diff0 == diff1:
            return diff0
    return -1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(alif(a))

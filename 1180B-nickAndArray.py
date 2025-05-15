# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1180/problem/B

def alif(a):
    n = len(a)
    if n % 2 == 0:
        modified_a = [min(x, -1 - x) for x in a]
    else:
        max_val = float('-inf')
        max_index = -1
        for i in range(n):
            current_val = max(a[i], -1 - a[i])
            if current_val > max_val:
                max_val = current_val
                max_index = i
        modified_a = [min(x, -1 - x) if i != max_index else max(x, -1 - x) for i, x in enumerate(a)]
    return " ".join(map(str, modified_a))

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(alif(a))

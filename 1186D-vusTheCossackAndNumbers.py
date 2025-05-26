# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1186/problem/D

def alif():
    n = int(input())
    a = [0.0] * n
    b = [0] * n
    total_sum = 0

    for p in range(n):
        val_a = float(input())
        a[p] = val_a
        b[p] = int(val_a)
        if b[p] > a[p]:
            b[p] -= 1
        total_sum += b[p]

    for p in range(n):
        if a[p] <= b[p]:
            continue
        elif total_sum < 0:
            b[p] += 1
            total_sum += 1
        else:
            break

    for p in range(n):
        print(b[p])

if __name__ == "__main__":
    alif()

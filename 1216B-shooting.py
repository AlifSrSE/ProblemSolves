# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1216/problem/B

def alif():
    n = int(input())
    a_values = list(map(int, input().split()))
    a = []

    for p in range(n):
        a.append((a_values[p], p + 1))
    a.sort(key=lambda x: x[0], reverse=True)
    total = n

    for p_idx in range(n):
        if p_idx > 0:
            total += p_idx * a[p_idx][0]
    
    print(total)

    for p_idx in range(n):
        print(a[p_idx][1], end=" ")
    print()

if __name__ == "__main__":
    alif()
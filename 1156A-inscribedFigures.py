# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1156/problem/A

def alif():
    n = int(input())
    a = list(map(int, input().split()))

    point_num = 0
    for i in range(1, n):
        if a[i] == 1:
            if a[i - 1] == 2:
                point_num += 3
            else:
                point_num += 4
        elif a[i] == 2:
            if a[i - 1] == 1:
                if i != 1 and a[i - 2] == 3:
                    point_num += 2
                else:
                    point_num += 3
            else:
                return "Infinite"
        elif a[i] == 3:
            if a[i - 1] == 1:
                point_num += 4
            else:
                return "Infinite"

    return f"Finite\n{point_num}"

if __name__ == "__main__":
    result = alif()
    print(result)
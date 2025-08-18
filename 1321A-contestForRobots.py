# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1321/problem/A

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    petya_wins = 0
    vasya_wins = 0

    for i in range(n):
        if a[i] == 1 and b[i] == 0:
            petya_wins += 1
        elif a[i] == 0 and b[i] == 1:
            vasya_wins += 1

    if petya_wins == 0:
        print(-1)
    else:
        print((vasya_wins // petya_wins) + 1)

alif()
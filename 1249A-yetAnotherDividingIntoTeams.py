# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1249/problem/A

def alif():
    N_CONST = 101
    q = int(input())

    for _ in range(q):
        n = int(input())
        a = [False] * N_CONST 
        numbers = list(map(int, input().split()))

        for x in numbers:
            a[x] = True
        both = False
        
        for p in range(1, N_CONST):
            if a[p - 1] and a[p]:
                both = True
                break
        print(1 + both)

if __name__ == "__main__":
    alif()
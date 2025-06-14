# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1209/problem/A

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    result = 0
    used = [False] * n
    
    for i in range(n):
        if not used[i]:
            result += 1
            for j in range(i, n):
                if a[j] % a[i] == 0:
                    used[j] = True
    print(result)

if __name__ == "__main__":
    alif()
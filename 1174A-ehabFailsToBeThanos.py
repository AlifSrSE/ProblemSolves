# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1174/problem/A

def alif(a):
    if len(set(a)) == 1:
        return "-1"
    else:
        a.sort()
        return " ".join(map(str, a))

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(alif(a))

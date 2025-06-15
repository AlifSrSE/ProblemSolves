# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1216/problem/A

def alif():
    n = int(input())
    s = list(input())
    cnt = 0

    for p in range(1, n, 2):
        if s[p] == s[p - 1]:
            s[p] = 'b' if s[p - 1] == 'a' else 'a'
            
            cnt += 1
    print(cnt)
    print("".join(s))

if __name__ == "__main__":
    alif()
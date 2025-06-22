# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1230/problem/B

def alif():
    n, k = map(int, input().split())
    s_list = list(input())

    if k == 0:
        print("".join(s_list))
    elif n == 1:
        print("0")
    else:
        if s_list[0] != '1':
            s_list[0] = '1'
            k -= 1
        for p in range(1, n):
            if k == 0:
                break
            
            if s_list[p] == '0':
                continue
            else:
                s_list[p] = '0'
                k -= 1
        print("".join(s_list))

if __name__ == "__main__":
    alif()
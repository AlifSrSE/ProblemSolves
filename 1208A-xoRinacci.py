# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1208/problem/A

def alif():
    T = int(input())
    
    for _ in range(T):
        a, b, n = map(int, input().split())
        remainder = n % 3
        if remainder == 0:
            result = a
        elif remainder == 1:
            result = b
        else:
            result = a ^ b
        print(result)

if __name__ == "__main__":
    alif()
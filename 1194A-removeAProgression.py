# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1194/problem/A

def alif():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n, x = map(int, input().split())
        print(2 * x)

if __name__ == "__main__":
    alif()
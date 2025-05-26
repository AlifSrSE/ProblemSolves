# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1187/problem/A

def alif():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n, s, t = map(int, input().split())
        result = 1 + n - (s if s < t else t)
        print(result)

if __name__ == "__main__":
    alif()
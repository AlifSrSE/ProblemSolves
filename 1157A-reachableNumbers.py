# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1156/problem/A

def f(x):
    result = x + 1
    while result % 10 == 0:
        result //= 10
    return result

def alif(n):
    history = set()
    while n not in history:
        history.add(n)
        n = f(n)
    return len(history)

if __name__ == "__main__":
    n = int(input())
    print(alif(n))
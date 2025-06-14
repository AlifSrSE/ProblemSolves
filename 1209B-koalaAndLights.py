# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1209/problem/B

def alif():
    n = int(input())
    s = input().strip()
    a = []
    b = []

    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    LIMIT = 125
    states = [c == '1' for c in s]
    result = sum(states)
    
    for step in range(LIMIT):
        for i in range(n):
            b[i] -= 1
            if b[i] == 0:
                states[i] = not states[i]
                b[i] = a[i]
        result = max(result, sum(states))
    print(result)

if __name__ == "__main__":
    alif()
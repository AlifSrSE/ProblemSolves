# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1173/problem/B

def alif(n):
    m = n // 2 + 1
    pairs = [(max(1, i - m + 2), min(m, i + 1)) for i in range(n)]
    result = "\n".join(f"{p[0]} {p[1]}" for p in pairs)
    return f"{m}\n{result}"

if __name__ == "__main__":
    n = int(input())
    print(alif(n))

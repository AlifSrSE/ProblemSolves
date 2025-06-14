# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1214/problem/C

def alif():
    _ = int(input())
    s = input().strip()
    depth = 0

    for ch in s:
        if ch == '(':
            depth += 1
        else:
            depth -= 1
            if depth < -1:
                print("No")
                return
    print("Yes" if depth == 0 else "No")

if __name__ == "__main__":
    alif()
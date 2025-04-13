# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, b):
    frees = set()
    index = 0
    for bi in b:
        if bi not in frees:
            if bi != a[index]:
                return False
            frees.add(a[index])
            index += 1
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, _ = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print("YA" if solve(a, b) else "TIDAK")
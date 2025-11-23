# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
input = sys.stdin.readline

def alif():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))

        even_indices = [i for i, x in enumerate(a) if x % 2 == 0]
        ok = False

        if len(even_indices) >= 2:
            print(a[even_indices[0]], a[even_indices[1]])
            ok = True
        else:
            for i in range(n):
                if ok:
                    break
                for j in range(i + 1, min(n, i + 60)):
                    if (a[j] % a[i]) % 2 == 0:
                        print(a[i], a[j])
                        ok = True
                        break

        if not ok:
            print(-1)

if __name__ == "__main__":
    alif()

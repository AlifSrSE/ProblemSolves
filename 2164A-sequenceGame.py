# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    ni_str = sys.stdin.readline()
    if not ni_str:
        return
    n = int(ni_str.strip())
    ai_line = sys.stdin.readline()

    if not ai_line:
        return
    a = list(map(int, ai_line.strip().split()))
    xi_line = sys.stdin.readline()

    if not xi_line:
        return
    x = int(xi_line.strip())

    if n == 1:
        if a[0] == x:
            print("YES")
        else:
            print("NO")
        return

    min_a = min(a)
    max_a = max(a)

    if min_a <= x <= max_a:
        print("YES")
    else:
        print("NO")


def main():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    T = int(t_str.strip())

    for _ in range(T):
        alif()

if __name__ == "__main__":
    main()
# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n, l, r):
    return "".join(str(i % 2) for i in range(n))

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    print(solve(n, l, r))

if __name__ == "__main__":
    main()
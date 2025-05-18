# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1184/problem/A1

def alif():
    ri = int(input())
    xi = 0
    yi = 0
    for wi in range(1, int(1e6) + 1):
        if wi * wi + 3 * wi + 1 > ri:
            break
        zi = (ri - wi * wi - wi - 1) // (2 * wi)
        if wi * wi + 2 * wi * zi + wi + 1 == ri:
            xi = wi
            yi = zi
            break

    if xi > 0 and yi >= 0:
        print(xi, yi)
    else:
        print("NO")

if __name__ == "__main__":
    alif()
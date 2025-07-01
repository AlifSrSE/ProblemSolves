# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1241/problem/B

def alif():
    q = int(input())

    for _ in range(q):
        s = input()
        t = input()
        set_s = set(s)
        set_t = set(t)
        possible = False

        for char_s in set_s:
            if char_s in set_t:
                possible = True
                break

        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()
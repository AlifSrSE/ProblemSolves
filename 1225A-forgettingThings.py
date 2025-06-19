# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1225/problem/A

def alif():
    da, db = map(int, input().split())
    if da == 9 and db == 1:
        print("9 10")
    elif da == db:
        print(f"{10 * da} {10 * da + 1}")
    elif db == da + 1:
        print(f"{10 * da + 9} {10 * (da + 1)}")
    else:
        print("-1")

if __name__ == "__main__":
    alif()
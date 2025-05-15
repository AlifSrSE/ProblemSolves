# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1181/problem/A

def alif(x, y, z):
    max_coconut_num = (x + y) // z
    if x % z + y % z >= z:
        min_exchange = z - max(x % z, y % z)
    else:
        min_exchange = 0
    return f"{max_coconut_num} {min_exchange}"

if __name__ == "__main__":
    x, y, z = map(int, input().split())
    print(alif(x, y, z))

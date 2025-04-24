# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1154/problem/A

def alif(x):
    x.sort()
    return ' '.join(str(x[-1] - x[i]) for i in range(len(x) - 1))

def main():
    x = list(map(int, input().split()))
    print(alif(x))

if __name__ == "__main__":
    main()

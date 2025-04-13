# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    a.sort()
    result = a[0]
    for i in range(1, len(a)):
        result = (result + a[i]) // 2
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
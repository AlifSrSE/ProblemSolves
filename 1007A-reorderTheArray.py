# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    a.sort()
    result = 0
    index_for_smaller = 0
    for i in range(len(a)):
        if a[i] > a[index_for_smaller]:
            result += 1
            index_for_smaller += 1
    return result

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == "__main__":
    main()
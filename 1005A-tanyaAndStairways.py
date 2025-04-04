# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    stairways = []
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            stairways.append(a[i])
    stairways.append(a[-1])
    return stairways

def main():
    n = int(input())
    a = list(map(int, input().split()))
    stairways = solve(a)
    print(len(stairways))
    print(" ".join(map(str, stairways)))

if __name__ == "__main__":
    main()
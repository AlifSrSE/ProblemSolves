def main():
    TC = int(input())
    for _ in range(TC):
        n = int(input())
        a = list(map(int, input().split()))
        
        isYes = True
        for i in range(n-2):
            if a[i] < 0:
                isYes = False
                break
            a[i+1] -= 2 * a[i]
            a[i+2] -= a[i]
            a[i] = 0
        if isYes and a[n-1] == 0 and a[n-2] == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
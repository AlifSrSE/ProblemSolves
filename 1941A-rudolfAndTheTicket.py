def main():
    TC = int(input()) 
    for _ in range(TC):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i] + b[j] <= k:
                    res += 1
                    
        print(res)

if __name__ == "__main__":
    main()
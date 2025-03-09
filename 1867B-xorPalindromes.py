def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        cnt = 0
        
        for p in range(n // 2):  
            if s[p] != s[n - 1 - p]:
                cnt += 1
        res = ['0'] * (n + 1)
    
        for p in range(cnt, n + 1):
            if p + cnt <= n:
                if n % 2 == 1 or (p - cnt) % 2 == 0:
                    res[p] = '1'
        
        print(''.join(res))

if __name__ == "__main__":
    main()
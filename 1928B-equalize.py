def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = []
        s = set()
        
        numbers = list(map(int, input().split()))
        for x in numbers:
            if x in s:
                continue
            v.append(x)
            s.add(x)
        
        v.sort()
        idx = 0
        ans = 0
        for p in range(len(v)):
            while idx + 1 < len(v) and v[idx + 1] < v[p] + n:
                idx += 1
            len_ = idx - p + 1
            ans = max(ans, len_)
            if idx + 1 == len(v):
                break
        
        print(ans)

if __name__ == "__main__":
    main()
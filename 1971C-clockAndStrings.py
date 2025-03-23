# Author: AlifSrSe
# date: 2025-03-19
# https://codeforces.com/problemset/problem/1971/C

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        aa = list(range(1, 13)) * 2
        ok = 0
        for i in range(len(aa)):
            if aa[i] == a:
                j = i + 1
                while j < len(aa) and aa[j] != b:
                    if aa[j] == c:
                        ok += 1
                    if aa[j] == d:
                        ok += 1
                    j += 1
                break
        if ok == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
# Author: AlifSrSe
# date: 2025-03-19
# https://codeforces.com/problemset/problem/1971/B

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if s.count(s[0]) == len(s):
            print("NO")
        else:
            s_list = list(s)
            for i in range(1, len(s)):
                if s[0] != s[i]:
                    s_list[0], s_list[i] = s_list[i], s_list[0]
                    break
            print("YES")
            print(''.join(s_list))

if __name__ == "__main__":
    main()
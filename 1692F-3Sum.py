# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/F

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip()) 
    
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        
        freq = {}
        mod = []
        for num in a:
            remainder = num % 10
            if freq.get(remainder, 0) < 3:
                mod.append(remainder)
            freq[remainder] = freq.get(remainder, 0) + 1

        n = len(mod)
        mod.sort()
        found = False
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (mod[i] + mod[j] + mod[k]) % 10 == 3:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        
        print("YES" if found else "NO")

if __name__ == "__main__":
    main()
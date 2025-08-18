# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1311/problem/C

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        p = list(map(int, sys.stdin.readline().split()))
        press_counts = [1] * n

        for pos in p:
            press_counts[pos - 1] += 1
            
        for i in range(n - 2, -1, -1):
            press_counts[i] += press_counts[i + 1]
        final_freq = [0] * 26

        for i in range(n):
            char_index = ord(s[i]) - ord('a')
            final_freq[char_index] += press_counts[i]
        print(*final_freq)

if __name__ == "__main__":
    alif()
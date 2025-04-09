# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
input = sys.stdin.readline

class XORSubarraySolver:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.a = []

    def read_input(self):
        self.n, self.k = map(int, input().split())
        self.a = list(map(int, input().split()))

    def find_minimum_length(self):
        if self.k == 0:
            return 1
        
        ans = float('inf')
        max_len = min(self.n, 64) 
        
        for i in range(self.n):
            if self.n - i >= ans:
                continue
            
            max_xor = 0
            for j in range(i + 1, min(self.n, i + max_len)):
                for p in range(i, j):
                    max_xor = max(max_xor, self.a[p] ^ self.a[j])
                if max_xor >= self.k:
                    ans = min(ans, j - i + 1)
                    break
        
        return -1 if ans == float('inf') else ans

def solve_test_case():
    solver = XORSubarraySolver()
    solver.read_input()
    print(solver.find_minimum_length())

def main():
    t = int(input())
    for _ in range(t):
        solve_test_case()

if __name__ == "__main__":
    main()
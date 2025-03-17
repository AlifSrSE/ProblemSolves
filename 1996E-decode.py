# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1996/problem/E

MODULUS = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    for _ in range(t):
        s = data[index]
        index += 1
        print(solve(s))

def solve(s):
    diff_to_left_sum = {0: 1}
    result = 0
    diff = 0
    for i in range(len(s)):
        diff += 1 if s[i] == '0' else -1
        result = add_mod(result, multiply_mod(diff_to_left_sum.get(diff, 0), len(s) - i))
        
        diff_to_left_sum[diff] = add_mod(diff_to_left_sum.get(diff, 0), i + 2)
    
    return result

def add_mod(x, y):
    return (x + y) % MODULUS

def multiply_mod(x, y):
    return (x * y) % MODULUS

if __name__ == "__main__":
    main()
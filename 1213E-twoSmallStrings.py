# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1213/problem/E
 
import sys
from itertools import permutations
 
def find_valid_string(n, s, t):
    p = "abc"
    for perm in permutations(p):
        p_str = "".join(perm)
        p1 = p_str + p_str
        if s not in p1 and t not in p1:
            return "YES\n" + (p_str * n)
        
        p2 = p_str[0] * n + p_str[1] * n + p_str[2] * n
        if s not in p2 and t not in p2:
            return "YES\n" + p2
    
    return "NO"
 
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    t = data[2]
    print(find_valid_string(n, s, t))
 
if __name__ == "__main__":
    main()